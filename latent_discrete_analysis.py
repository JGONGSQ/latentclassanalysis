from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
from lib.biologit_gen import problogit_gen, class_membership_gen

# Assuming the last option is fixed as the base alternative
number_of_alternatives = 3

# list_of_classes = ['A', 'B']
list_of_classes = ['A', 'B', 'C']

# alternative specific constant in each class
asc_variables = ['ASC_OPTION']

# class specific variables
class_variables = {
    "B_VEHICLE_PRICE": "alt#num#pr",
    "Range": "alt#num#rg",
    "R_time": "alt#num#ti",
    "Set_cost": "alt#num#se",
    "Cost_km": "alt#num#co",
    "Ava_fast": "alt#num#avl",
    "Acc_bus": "alt#num#acc",
    "Rebate_upfront_cost": "alt#num#incup",
    "Rebate_parking": "alt#num#incprk",
    "Energy_bill": "alt#num#incbll",
    "Stamp_duty": "alt#num#incst",
    "Penetration": "alt#num#sld",
    "Small_Sedan": "alt#num#vhtype",
    "Large_Sedan": "alt#num#vhtype",
    "Small_SUV": "alt#num#vhtype",
    "Large_SUV": "alt#num#vhtype",
    "Small_hatch": "alt#num#vhtype",
}

list_of_class_variables = [
    class_variables, 
    class_variables, 
    class_variables
    ]

# class with alternative specific variables
class_alternative_variables = {
    # "B_VEHICLE_PRICE": "alt#num#pr"
}

list_of_class_alternative_variables = [
    class_alternative_variables, 
    class_alternative_variables, 
    class_alternative_variables
    ]

category_variable = {
    "Small_Sedan": 1,
    "Large_Sedan": 2,
    "Small_SUV": 3,
    "Large_SUV": 4,
    "Small_hatch": 5
}

# the variables relates to the class membership
sociademographic_variables = {
    # "TEST_VARIABLE": "alt2co"
}

list_of_sociademographic_variables = [
    sociademographic_variables,
    sociademographic_variables,
    sociademographic_variables
]

scale_coefficient = {
    "alt#num#pr": 100000.0,
    "alt#num#rg": 100.0,
    "alt#num#ti": 10.0,
    "alt#num#se": 1000.0,
    "alt#num#co": 10.0,
    "alt#num#avl": 10.0,
    "alt#num#incup": 10000.0,
    "alt#num#incprk": 100.0,
    "alt#num#incbll": 100.0,
    "alt#num#incst": 10.0,
    "alt#num#sld": 100.0
}


probs = problogit_gen(
    asc_variables, 
    list_of_class_variables, 
    list_of_class_alternative_variables,
    category_variable,
    scale_coefficient,
    number_of_alternatives,
    list_of_classes
    )

print("This is the probs #############", probs)

# Define the panel ObsIter String
panelObsIter = 'panelObsIter'

class_membership = class_membership_gen(list_of_classes, list_of_sociademographic_variables, category_variable, panelObsIter, scale_coefficient)

# Define the metaIterator
metaIterator('personIter', '__dataFile__', 'panelObsIter', 'id')

# Defines an itertor on the data
rowIterator('panelObsIter', 'personIter')

#TODO corss product between to lists might have a better way to do it
for i, prob in enumerate(probs):
    if i == 0:
        probIndiv = Prod(prob, panelObsIter) * class_membership[i]
    else:
        probIndiv += Prod(prob, panelObsIter) * class_membership[i]

loglikelihood = Sum(log(probIndiv),'personIter')
BIOGEME_OBJECT.ESTIMATE = loglikelihood

BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"
BIOGEME_OBJECT.PARAMETERS['checkDerivatives'] = "0" #0 is faster
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = "30"
