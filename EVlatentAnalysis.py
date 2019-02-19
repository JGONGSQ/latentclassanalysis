########################################
#
# @file 01logit.py
# @author: Michel Bierlaire, EPFL
# @date: Wed Dec 21 13:23:27 2011
#
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

# Parameters to be estimated
# Arguments:
#   - 1  Name for report; Typically, the same as the variable.
#   - 2  Starting value.
#   - 3  Lower bound.
#   - 4  Upper bound.
#   - 5  0: estimate the parameter, 1: keep it fixed.

ASC_OPTION1_A = Beta('ASC_OPTION1_A',0.5,-10,10,0,'OPTION1 constant;')
ASC_OPTION2_A = Beta('ASC_OPTION2_A',0.5,-10,10,0,'OPTION2 constant;')
ASC_OPTION3_A = Beta('ASC_OPTION3_A',0.5,-10,10,1,'OPTION3 constant;')

B_VEHICLE_PRICE_A = Beta('B_VEHICLE_PRICE_A',0.5,-10,10,0,'Vehicle Price')
# B_VEHICLE_PRICE2 = Beta('B_VEHICLE_PRICE2',0,-10,10,0,'Vehicle Price 2')
# B_VEHICLE_PRICE3 = Beta('B_VEHICLE_PRICE3',0,-10,10,1,'Vehicle Price 3')
# B_VEHICLE_TYPE = Beta('B_VEHICLE_TYPE',0,-10,10,0,'Vehicle Type')
# B_VEHICLE_TYPE2 = Beta('B_VEHICLE_TYPE2',0,-10,10,0,'Vehicle Type 2')
# B_VEHICLE_TYPE3 = Beta('B_VEHICLE_TYPE3',0,-10,10,1,'Vehicle Type 3')

# Utility functions

#If the person has a GA (season ticket) her incremental cost is actually 0
#rather than the cost value gathered from the
# network data.

# SM_COST =  SM_CO   * (  GA   ==  0  )
# TRAIN_COST =  TRAIN_CO   * (  GA   ==  0  )

# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0.
# A previous estimation with the unscaled data has generated
# parameters around -0.01 for both cost and time. Therefore, time and
# cost are multipled my 0.01.

# The following statements are designed to preprocess the data. It is
# like creating a new columns in the data file. This should be
# preferred to the statement like
# TRAIN_TT_SCALED = TRAIN_TT / 100.0
# which will cause the division to be reevaluated again and again,
# throuh the iterations. For models taking a long time to estimate, it
# may make a significant difference.

VEHICLE_OPTION1_PRICE_SCALED = DefineVariable('VEHICLE_OPTION1_PRICE_SCALED', alt1pr / 1000.0)
VEHICLE_OPTION2_PRICE_SCALED = DefineVariable('VEHICLE_OPTION2_PRICE_SCALED', alt2pr / 1000.0)
# TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100)
# SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0)
# SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100)
# CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100)
# CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100)

V1A = ASC_OPTION1_A + B_VEHICLE_PRICE_A * VEHICLE_OPTION1_PRICE_SCALED
V2A = ASC_OPTION2_A + B_VEHICLE_PRICE_A * VEHICLE_OPTION2_PRICE_SCALED
V3A = ASC_OPTION3_A

# Associate utility functions with the numbering of alternatives
VA = {1: V1A,
     2: V2A,
     3: V3A}



# Associate the availability conditions with the alternatives
# CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ))
# TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ))

# av = {1: TRAIN_AV_SP,
#       2: SM_AV,
#       3: CAR_AV_SP}

avA = {1: 1,
      2: 1,
      3: 1}


# The choice model is a logit, with availability conditions
prob_A = bioLogit(VA, avA, choice)


###############################################################################################

ASC_OPTION1_B = Beta('ASC_OPTION1_B',0.5,-10,10,0,'OPTION1 constant;')
ASC_OPTION2_B = Beta('ASC_OPTION2_B',0.5,-10,10,0,'OPTION2 constant;')
ASC_OPTION3_B = Beta('ASC_OPTION3_B',0,-10,10,1,'OPTION3 constant;')

B_VEHICLE_PRICE_B = Beta('B_VEHICLE_PRICE_B',0.5,-10,10,0,'Vehicle Price')
# B_VEHICLE_PRICE2 = Beta('B_VEHICLE_PRICE2',0,-10,10,0,'Vehicle Price 2')
# B_VEHICLE_PRICE3 = Beta('B_VEHICLE_PRICE3',0,-10,10,1,'Vehicle Price 3')
# B_VEHICLE_TYPE = Beta('B_VEHICLE_TYPE',0,-10,10,0,'Vehicle Type')
# B_VEHICLE_TYPE2 = Beta('B_VEHICLE_TYPE2',0,-10,10,0,'Vehicle Type 2')
# B_VEHICLE_TYPE3 = Beta('B_VEHICLE_TYPE3',0,-10,10,1,'Vehicle Type 3')

# Utility functions

#If the person has a GA (season ticket) her incremental cost is actually 0
#rather than the cost value gathered from the
# network data.

# SM_COST =  SM_CO   * (  GA   ==  0  )
# TRAIN_COST =  TRAIN_CO   * (  GA   ==  0  )

# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0.
# A previous estimation with the unscaled data has generated
# parameters around -0.01 for both cost and time. Therefore, time and
# cost are multipled my 0.01.

# The following statements are designed to preprocess the data. It is
# like creating a new columns in the data file. This should be
# preferred to the statement like
# TRAIN_TT_SCALED = TRAIN_TT / 100.0
# which will cause the division to be reevaluated again and again,
# throuh the iterations. For models taking a long time to estimate, it
# may make a significant difference.

# VEHICLE_OPTION1_PRICE_SCALED = DefineVariable('VEHICLE_OPTION1_PRICE_SCALED', alt1pr / 1000.0)
# VEHICLE_OPTION2_PRICE_SCALED = DefineVariable('VEHICLE_OPTION2_PRICE_SCALED', alt2pr / 1000.0)
# TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100)
# SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0)
# SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100)
# CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100)
# CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100)

V1B = ASC_OPTION1_B + B_VEHICLE_PRICE_B * VEHICLE_OPTION1_PRICE_SCALED
V2B = ASC_OPTION2_B + B_VEHICLE_PRICE_B * VEHICLE_OPTION2_PRICE_SCALED
V3B = ASC_OPTION3_B

# Associate utility functions with the numbering of alternatives
VB = {1: V1B,
     2: V2B,
     3: V3B}



# Associate the availability conditions with the alternatives
# CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ))
# TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ))

# av = {1: TRAIN_AV_SP,
#       2: SM_AV,
#       3: CAR_AV_SP}

avB = {1: 1,
      2: 1,
      3: 1}


# The choice model is a logit, with availability conditions
prob_B = bioLogit(VB, avB, choice)

#################################################################################################


################################### CLASS MEMBERSHIP ############################################
CLASS_A = Beta('CLASS_A',0.5,-10,10,0,'CLASS A')
CLASS_B = Beta('CLASS_B',0,-10,10,1,'CLASS B')

# age = beta()
# prob_A = CLASS_A + age
prob1 = CLASS_A
prob2 = CLASS_B

probClass1 = exp(prob1)/(exp(prob1) + exp(prob2))
probClass2 = 1 - probClass1


probClass11 = Sum(probClass1, 'panelObsIter')/Sum(1, 'panelObsIter')
probClass22 = Sum(probClass2, 'panelObsIter')/Sum(1, 'panelObsIter')
# caseid starts from 1 to 1076
metaIterator('personIter', '__dataFile__','panelObsIter', 'caseid')

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

#BIOGEME_OBJECT.FORMULAS['Option1 utility'] = V1
#BIOGEME_OBJECT.FORMULAS['Option2 utility'] = V2
#BIOGEME_OBJECT.FORMULAS['Option3 utility'] = V3
