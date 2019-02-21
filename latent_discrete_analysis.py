from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
from lib.biologit_gen import problogit_gen, class_membership_gen


ASC_OPTION1 = Beta('ASC_OPTION1', 0.5, -10, 10, 0, 'OPTION1 constant;')
ASC_OPTION2 = Beta('ASC_OPTION2', 0.5, -10, 10, 0, 'OPTION2 constant;')
ASC_OPTION3 = Beta('ASC_OPTION3', 0.5, -10, 10, 1, 'OPTION3 constant;')

# Assuming the last option is fixed as the base alternative
number_of_alternatives = 3

# list_of_classes = ['A']
list_of_classes = ['A', 'B', 'C']

# alternative specific constant in each class
asc_variables = ['ASC_OPTION']

# class specific variables
class_variables = {
    "B_VEHICLE_PRICE": "alt#num#pr"
}


# class with alternative specific variables
class_alternative_variables = {
    # "B_VEHICLE_PRICE": "alt#num#pr"
}

scale_coefficient = {
    "alt#num#pr": 10000.0
}

# the variables relates to the class membership
sociademographic_variables = {

}

probs = problogit_gen(
    asc_variables, 
    class_variables, 
    class_alternative_variables,
    scale_coefficient,
    number_of_alternatives,
    list_of_classes
    )

print("This is the probs #############", probs)


panelObsIter = 'panelObsIter'

class_membership = class_membership_gen(list_of_classes, sociademographic_variables, panelObsIter)


metaIterator('personIter', '__dataFile__', 'panelObsIter', 'id')

# Defines an itertor on the data
rowIterator('panelObsIter', 'personIter')


for i, prob in enumerate(probs):
    if i == 0:
        probIndiv = Prod(prob, panelObsIter) * class_membership[i]
    else:
        probIndiv += Prod(prob, panelObsIter) * class_membership[i]

loglikelihood = Sum(log(probIndiv),'personIter')
BIOGEME_OBJECT.ESTIMATE = loglikelihood

BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"
