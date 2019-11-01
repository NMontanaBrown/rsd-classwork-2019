#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:16:53 2019

@author: nina
Exercise to test multiple ranges on both inputs
"""
from testing import overlap_time, time_range, time_diff_min

def test_given_input():

        large = time_range("2010-01-12 00:00:00", "2010-01-12 23:50:00", 24, 600) #24 segments with 10 min breaks
        short = time_range("2010-01-12 00:30:00", "2010-01-12 23:55:00", 24, 2100) #24 segments with 35 min breaks
        
        result = (overlap_time(large, short))
        # overlap should be the minutes 30-50 on the hour
        # should return a list of 24 hour segments 
        # however the first ends at midnight so 23 segments
        
        # we need to assert that the difference between the two values is 20 mins
        
        # overlap time function can't handle both ranges having gaps
        # currently returns True, False, False....
        # need to edit the overlap time function
        
        assert all([(time_diff_min(tup[0], tup[1]) == 20) for tup in result])
        
        # asserting all elements in unpacked tuple matches our requirement.
    
