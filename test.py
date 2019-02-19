from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
from lib.biologit_gen import problogit_gen


ASC_OPTION1 = Beta('ASC_OPTION1', 0.5, -10, 10, 0, 'OPTION1 constant;')
ASC_OPTION2 = Beta('ASC_OPTION2', 0.5, -10, 10, 0, 'OPTION2 constant;')
ASC_OPTION3 = Beta('ASC_OPTION3', 0.5, -10, 10, 1, 'OPTION3 constant;')

variables = [ASC_OPTION1, ASC_OPTION2, ASC_OPTION3]

problogit_gen(variables)