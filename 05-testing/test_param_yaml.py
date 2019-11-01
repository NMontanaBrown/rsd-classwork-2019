#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:06:21 2019

@author: nina

Testing how to run automated tests using a yaml file
"""
import yaml
import pytest 
from testing import overlap_time, time_range

## reading the yaml file
    
with open('testcases.yaml') as yaml_testcases_in:
    testcases_testing = yaml.safe_load(yaml_testcases_in)

# In the inverted commas you get the arguments to be used
# in the tuple you should encounter the pairs of items you want to test

cases = ['no_overlap']

# The example below is the no_overlap case where an empty tuple should be returned.
@pytest.mark.parametrize("cases, large, small, expected", 
                         [(time_range(testcases_testing[cases]['large'][0], testcases_testing[cases]['large'][1], testcases_testing[cases]['large'][2], testcases_testing[cases]['large'][3]),
                          time_range(testcases_testing[cases]['small'][0], testcases_testing[cases]['small'][1], testcases_testing[cases]['small'][2], testcases_testing[cases]['small'][3]), 
                          testcases_testing[cases]['expected'][0])] )

# defining the test
# it will run for all the tuple groups defined above
def test_eval(cases,large, small, expected):
    assert (overlap_time(large, small)) == expected