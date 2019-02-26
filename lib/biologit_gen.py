from biogeme import *
from headers import *

LOWER_LIMIT = -10.0
UPPER_LIMIT = 10.0


def adding_variables_to_utility_equation(
    base_variable, variable_dict, category_variable,
    scale_coefficient, class_item, index, number_of_alternatives, 
    initial_value, is_fixed, is_indexed):

    utility_equation = base_variable

    if is_indexed:
        variable_name_index = index
    else:
        variable_name_index = ""
    
    # class alternative specific variables
    for k, v in variable_dict.items():
        print("this is the k v pair", k, v)
        beta = Beta(
            '{var_name}_{index}_{class_item}'.format(
                var_name=k,
                index=variable_name_index, 
                class_item=class_item),
            initial_value, LOWER_LIMIT, UPPER_LIMIT, is_fixed,
            '{var_name}_{index}_{class_item}'.format(
                var_name=k,
                index=variable_name_index,
                class_item=class_item)
            )

        if v in scale_coefficient:
            scale = scale_coefficient[v]
        else:
            scale = 1

        if "#num#" in v:
            variable_name = v.replace("#num#", str(index))
        else:
            variable_name = v

        variable = DefineVariable(
            '{var_name}_SCALED'.format(var_name=variable_name),
            Variable(variable_name)/scale
            )

        if index != number_of_alternatives:
            if k in category_variable:
                utility_equation += beta * (variable == category_variable[k])
            else:
                utility_equation += beta * variable

    return utility_equation



def problogit_gen(
    asc_variables, 
    class_variables, 
    class_alternative_variables, 
    category_variable,
    scale_coefficient, 
    number_of_alternatives, 
    list_of_classes):

    probs = list()
    
    for class_item in list_of_classes:
        V = {}
        av = {}
        print(class_item)
        
        for i in range(number_of_alternatives):
            local_index = i + 1
            
            # alternative specific constant
            if  local_index == number_of_alternatives:
                is_fixed = 1
                initial_value = 0.0
            else:
                is_fixed = 0 
                initial_value = 0.5    
            
            alt_V = Beta(
                '{var_name}_{index}_{class_item}'.format(
                    var_name=asc_variables[0], 
                    index=local_index, 
                    class_item=class_item), 
                initial_value, LOWER_LIMIT, UPPER_LIMIT, is_fixed, 
                '{var_name}_{index}_{class_item} constant'.format(
                    var_name=asc_variables[0], 
                    index=local_index, 
                    class_item=class_item)
                )

            alt_V = adding_variables_to_utility_equation(
                base_variable=alt_V,
                variable_dict=class_variables,
                category_variable=category_variable,
                scale_coefficient=scale_coefficient,
                class_item=class_item,
                index=local_index,
                number_of_alternatives=number_of_alternatives,
                initial_value=initial_value,
                is_fixed=is_fixed,
                is_indexed=False
            )

            # class alternative specific variables
            alt_V = adding_variables_to_utility_equation(
                base_variable=alt_V,
                variable_dict=class_alternative_variables,
                category_variable=category_variable,
                scale_coefficient=scale_coefficient,
                class_item=class_item,
                index=local_index,
                number_of_alternatives=number_of_alternatives,
                initial_value=initial_value,
                is_fixed=is_fixed,
                is_indexed=True
            )

            print("This is the alternative utility", alt_V)
            
            V[local_index] = alt_V
            av[local_index] = 1

        probs.append(bioLogit(V,av, choice))

    return probs



def class_membership_gen(
    list_of_classes, 
    sociademographic_variables, 
    category_variable,
    panelObsIter, 
    scale_coefficient):

    class_variables = list()
    probsClass = list()
    
    for i, class_item in enumerate(list_of_classes):
        local_index = i + 1
        
        if local_index == len(list_of_classes):
            is_fixed = 1
            initial_value = 0
        else:
            is_fixed = 0
            initial_value = 0.5

        class_beta = Beta(
            'CLASS_{class_item}'.format(class_item=class_item),
            initial_value, LOWER_LIMIT, UPPER_LIMIT, is_fixed, 
            'CLASS_{class_item}'.format(class_item=class_item)
            )

        # adding sociademograohic variables to the class membership utility function
        class_beta = adding_variables_to_utility_equation(
                base_variable=class_beta,
                variable_dict=sociademographic_variables,
                category_variable=category_variable,
                scale_coefficient=scale_coefficient,
                class_item=class_item,
                index=local_index,
                number_of_alternatives=len(list_of_classes),
                initial_value=initial_value,
                is_fixed=is_fixed,
                is_indexed=False
            )

        class_variables.append(class_beta)
    
    # calcualte the denominator for the class membership
    for i, variable in enumerate(class_variables):
        if i == 0:
            denominator = exp(variable) 
        else:
            denominator += exp(variable)


    for variable in class_variables:
        prob_class = Sum(exp(variable)/denominator, panelObsIter)/Sum(1, panelObsIter)
        probsClass.append(prob_class)


    print("This is the probsClass", probsClass)

    return probsClass

    

        

