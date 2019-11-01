#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:43:01 2019

@author: nina

Creating a YAML File to include all test cases
"""

import yaml
from testing import overlap_time, time_range

# creating the data structure to be written into yaml
testcases =  {'no_overlap': 
                    {'large': ["2010-01-12 00:00:00", "2010-01-12 23:50:00", 2, 600],
                    'small': ["2010-01-13 00:00:00", "2010-01-13 23:50:00", 2, 600],
                    'expected': "[]"
                     }
#             'edge_case': 
#                    {'large': 
#                        time_range("2010-01-12 00:00:00", "2010-01-12 00:50:00", 3, 600),
#                    'small': time_range("2010-01-12 00:10:00", "2010-01-12 01:00:00", 3, 600),
#                    'expected': "[('2010-01-12 00:10:00', '2010-01-12 00:10:00'), ('2010-01-12 00:20:00', '2010-01-12 00:20:00'), ('2010-01-12 00:30:00', '2010-01-12 00:30:00'), ('2010-01-12 00:40:00', '2010-01-12 00:40:00'), ('2010-01-12 00:50:00', '2010-01-12 00:50:00')]"
#                    },
             }


                    
        
# writing it to yaml format
with open('testcases.yaml', 'w') as yaml_testcases_out:
    yaml_testcases_out.write(yaml.dump(testcases))

## reading it in yaml
    
with open('testcases.yaml') as yaml_testcases_in:
    testcases_testing = yaml.safe_load(yaml_testcases_in)

#  Checking correct output  

#print(testcases_testing)

#print(testcases_testing['no_overlap']['expected'])