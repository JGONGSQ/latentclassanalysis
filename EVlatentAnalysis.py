########################################
#
# @file EVlatentAnalysis.py
# @author: James Gong, Ali
# @date: 19 Feb 2019
#
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

############ Defined Variables #############################
VEHICLE_OPTION1_PRICE_SCALED = DefineVariable('VEHICLE_OPTION1_PRICE_SCALED', alt1pr / 10000.0)
VEHICLE_OPTION2_PRICE_SCALED = DefineVariable('VEHICLE_OPTION2_PRICE_SCALED', alt2pr / 10000.0)


######################################## Class A #############################################
ASC_OPTION1_A = Beta('ASC_OPTION1_A', 0.5, -10, 10, 0, 'OPTION1 constant;')
ASC_OPTION2_A = Beta('ASC_OPTION2_A', 0.5, -10, 10, 0, 'OPTION2 constant;')
ASC_OPTION3_A = Beta('ASC_OPTION3_A', 0, -10, 10, 1,'OPTION3 constant;')

B_VEHICLE_PRICE_A = Beta('B_VEHICLE_PRICE_A', 0.5, -10, 10, 0, 'Vehicle Price')

# Utility functions
V1A = ASC_OPTION1_A + B_VEHICLE_PRICE_A * VEHICLE_OPTION1_PRICE_SCALED
V2A = ASC_OPTION2_A + B_VEHICLE_PRICE_A * VEHICLE_OPTION2_PRICE_SCALED
V3A = ASC_OPTION3_A
print("####################### This is the V1A", V1A)
print("####################### This is the V1A", V3A)
# Associate utility functions with the numbering of alternatives
VA = {
    1: V1A,
    2: V2A,
    3: V3A
}


avA = {
    1: 1,
    2: 1,
    3: 1
}


# The choice model is a logit, with availability conditions
prob_A = bioLogit(VA, avA, choice)


########################### Class B ###################################################

ASC_OPTION1_B = Beta('ASC_OPTION1_B', 0.5, -10, 10, 0, 'OPTION1 constant;')
ASC_OPTION2_B = Beta('ASC_OPTION2_B', 0.5, -10, 10, 0, 'OPTION2 constant;')
ASC_OPTION3_B = Beta('ASC_OPTION3_B', 0, -10, 10, 1, 'OPTION3 constant;')

B_VEHICLE_PRICE_B = Beta('B_VEHICLE_PRICE_B', 0.5, -10, 10, 0, 'Vehicle Price')

# Utility functions
V1B = ASC_OPTION1_B + B_VEHICLE_PRICE_B * VEHICLE_OPTION1_PRICE_SCALED
V2B = ASC_OPTION2_B + B_VEHICLE_PRICE_B * VEHICLE_OPTION2_PRICE_SCALED
V3B = ASC_OPTION3_B

# Associate utility functions with the numbering of alternatives
VB = {
    1: V1B,
    2: V2B,
    3: V3B
}

avB = {
    1: 1,
    2: 1,
    3: 1 
}


# The choice model is a logit, with availability conditions
prob_B = bioLogit(VB, avB, choice)

################################### CLASS MEMBERSHIP ############################################
CLASS_A = Beta('CLASS_A', 0.5, -10, 10, 0, 'CLASS A')
CLASS_B = Beta('CLASS_B', 0, -10, 10, 1, 'CLASS B')

# age = beta()
# prob_A = CLASS_A + age
prob1 = CLASS_A
prob2 = CLASS_B

probClass1 = exp(prob1)/(exp(prob1) + exp(prob2))
probClass2 = exp(prob2)/(exp(prob1) + exp(prob2))
# probClass2 = 1 - probClass1

probClass11 = Sum(probClass1, 'panelObsIter')/Sum(1, 'panelObsIter')
probClass22 = Sum(probClass2, 'panelObsIter')/Sum(1, 'panelObsIter')

# id starts from 1 to 1076
metaIterator('personIter', '__dataFile__','panelObsIter', 'id')

# Defines an itertor on the data
rowIterator('panelObsIter', 'personIter')

#Conditional probability for the sequence of choices of an individual
condProbIndiv1 = Prod(prob_A,'panelObsIter')
condProbIndiv2 = Prod(prob_B,'panelObsIter')
 
# probability of individual belonging to a class
probIndiv = (probClass11*condProbIndiv1) + (probClass22*condProbIndiv2)

# DEfine the likelihood function for the estimation 
# Likelihood function
loglikelihood = Sum(log(probIndiv),'personIter')
BIOGEME_OBJECT.ESTIMATE = loglikelihood


# All observations verifying the following expression will not be
# considered for estimation
# The modeler here has developed the model only for work trips.
# Observations such that the dependent variable CHOICE is 0 are also removed.
# exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) + ( CHOICE == 0 )) > 0

# BIOGEME_OBJECT.EXCLUDE = exclude

# Statistics

# nullLoglikelihood(av,'obsIter')
# choiceSet = [1,2,3]
# cteLoglikelihood(choiceSet,choice,'obsIter')
# availabilityStatistics(av,'obsIter')


BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"