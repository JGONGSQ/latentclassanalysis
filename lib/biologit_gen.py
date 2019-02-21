from biogeme import *
from headers import *



def problogit_gen(asc_variables, class_variables, class_alternative_variables, scale_coefficient, number_of_alternatives, list_of_classes):
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
                initial_value, -10, 10, is_fixed, 
                '{var_name}_{index}_{class_item} constant'.format(
                    var_name=asc_variables[0], 
                    index=local_index, 
                    class_item=class_item)
                )

            # class specific variables
            for k, v in class_variables.items():
                beta = Beta(
                    '{var_name}_{class_item}'.format(
                        var_name=k, 
                        class_item=class_item),
                    initial_value, -10, 10, is_fixed,
                    '{var_name}_{class_item}'.format(
                        var_name=k, 
                        class_item=class_item)
                    )

                if v in scale_coefficient:
                    scale = scale_coefficient[v]
                else:
                    scale = 1
                variable_name = v.replace("#num#", str(local_index))
                variable = DefineVariable(
                    '{var_name}_SCALED'.format(var_name=variable_name),
                    Variable(variable_name)/scale
                    )

                if local_index != number_of_alternatives:
                    alt_V += beta * variable

            # class alternative specific variables
            for k, v in class_alternative_variables.items():
                print("this is the k v pair", k, v)
                beta = Beta(
                    '{var_name}_{index}_{class_item}'.format(
                        var_name=k,
                        index=local_index, 
                        class_item=class_item),
                    initial_value, -10, 10, is_fixed,
                    '{var_name}_{index}_{class_item}'.format(
                        var_name=k,
                        index=local_index,
                        class_item=class_item)
                    )

                if v in scale_coefficient:
                    scale = scale_coefficient[v]
                else:
                    scale = 1
                variable_name = v.replace("#num#", str(local_index))
                variable = DefineVariable(
                    '{var_name}_SCALED'.format(var_name=variable_name),
                    Variable(variable_name)/scale
                    )

                if local_index != number_of_alternatives:
                    alt_V += beta * variable

            print("This is the alternative utility", alt_V)
            
            V[local_index] = alt_V
            av[local_index] = 1

        probs.append(bioLogit(V,av, choice))

    return probs



def class_membership_gen(list_of_classes, sociademographic_variables, panelObsIter):
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
            initial_value, -10, 10, is_fixed, 
            'CLASS_{class_item}'.format(class_item=class_item)
            )

        # insert social demographic variables here
        # class_beta += age + gender....

        class_variables.append(class_beta)
    
    # calcualte the denominator for the class membership
    for i, variable in enumerate(class_variables):
        if i == 0:
            denominator = exp(variable) 
        else:
            denominator += exp(variable)

    # print("This is the denominator $$$$$$$$$$$$$$", denominator)

    for variable in class_variables:
        prob_class = Sum(exp(variable)/denominator, panelObsIter)/Sum(1, panelObsIter)
        probsClass.append(prob_class)


    print("This is the probsClass", probsClass)

    return probsClass

    

        

