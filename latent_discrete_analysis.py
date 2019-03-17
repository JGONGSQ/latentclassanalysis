from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
from lib.biologit_gen import problogit_gen, class_membership_gen

# Assuming the last option is fixed as the base alternative
number_of_alternatives = 3

# list_of_classes = ['A', 'B']
# list_of_classes = ['A', 'B', 'C', 'D', 'E', 'F']
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

class_variables_B = {
    # "B_VEHICLE_PRICE": "alt#num#pr",
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
    # "Large_SUV": "alt#num#vhtype",
    "Small_hatch": "alt#num#vhtype",
}

class_variables_D = {
    # "B_VEHICLE_PRICE": "alt#num#pr",
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

class_variables_E = {
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

class_variables_F = {
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

class_variables_G = {
    # "B_VEHICLE_PRICE": "alt#num#pr",
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
    class_variables_B, 
    class_variables,
    # class_variables_D,
    # class_variables_E,
    # class_variables_F
    # class_variables_G
    ]

# class with alternative specific variables
class_alternative_variables = {
    # "B_VEHICLE_PRICE": "alt#num#pr"
}

list_of_class_alternative_variables = [
    class_alternative_variables, 
    class_alternative_variables, 
    # class_alternative_variables,
    # class_alternative_variables,
    # class_alternative_variables,
    class_alternative_variables
    # class_alternative_variables
    ]

category_variable = {
    "Small_Sedan": 1,
    "Large_Sedan": 2,
    "Small_SUV": 3,
    "Large_SUV": 4,
    "Small_hatch": 5,
    "Gender_male" : 1,
    "Gender_female" : 2,
    "Gender_other" : 3,
    "Lifestyle_Couple": 1,
    "Lifestyle_Couple_with_kid": 2,
    "Lifestyle_OneParent_with_kid": 3,
    "Lifestyle_Other": 4,
    "Lifestyle_Single": 5,
    "Lifestyle_Group": 6,
     "Employment_fulltime": 1,
    "Employment_parttime": 2,
    "Employment_unemployed_looking": 3,
    "Employment_unemployed": 4,
    "Employment_retired": 5,
    "Employment_student": 6,
    "Employment_household": 7,
    "Education_PhD": 1,
    "Education_Master": 2,
    "Education_GraduateDiploma": 3,
    "Education_Bachelor": 4,
    "Education_Diploma": 5,
    "Education_TAFE": 6,
    "Education_Year12": 7,
    "Education_UnderYear12": 8,
    "NumCars_1": 1,
    "NumCars_2": 2,
    "NumCars_2+": 3,
    "isLicenced_Yes": 1,
    "isLicenced_No": 2,
    "householdtype_freestanding": 1,
    "householdtype_townhouse": 2,
    "householdtype_apartment": 3,
    "householdtype_other": 4,
    "dwelling_own_outright": 1,
    "dwelling_own_mortgage": 2,
}

# the variables relates to the class membership
sociademographic_variables = {
    # "Gender_male": "gender",
    # "Gender_female": "gender",
    # "Gender_other": "gender"
    # "Lifestyle_Couple": "lifestyle",
    # "Lifestyle_Couple_with_kid": "lifestyle",
    # "Lifestyle_OneParent_with_kid": "lifestyle",
    # "Lifestyle_Other": "lifestyle",
    # "Lifestyle_Single": "lifestyle",
    # "Lifestyle_Group": "lifestyle",
    # "Employment_fulltime": "employment", # may woprks
    # "Employment_parttime": "employment",
    # "Employment_unemployed_looking": "employment",
    # "Employment_unemployed": "employment",
    # "Employment_retired": "employment",
    # "Employment_student": "employment",
    # "Employment_household": "employment",
    # "Education_PhD": "education",
    # "Education_Master": "education",
    # "Education_GraduateDiploma": "education",
    # "Education_Bachelor": "education",
    # "Education_Diploma": "education",
    # "Education_TAFE": "education",
    # "Education_Year12": "education",
    # "Education_UnderYear12": "education",
    # "NumCars_1": "numCars", # may works
    # "NumCars_2": "numCars",
    # "NumCars_2+": "numCars",
    # "isLicenced_Yes": "isLicenced",
    # "isLicenced_No": "isLicenced",
    # "numberHousehold": "numHousehold", # mayworks
    # "householdtype_freestanding": "householdtype",
    # "householdtype_townhouse": "householdtype",
    # "householdtype_apartment": "householdtype",
    # "householdtype_other": "householdtype",
    "dwelling_own_outright": "dwelling",
    "dwelling_own_mortgage": "dwelling",
    
}

list_of_sociademographic_variables = [
    sociademographic_variables,
    sociademographic_variables,
    # sociademographic_variables,
    # sociademographic_variables,
    # sociademographic_variables,
    # sociademographic_variables,
    sociademographic_variables
]

scale_coefficient = {
    "alt#num#pr": 10000.0,
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
