#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:11:31 2019

@author: nina

test_class_time 
"""

from testing import overlap_time, time_range

def test_given_input():

        large = time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
        short = time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600) #3 segments with 10 min breaks
        result = (overlap_time(large, short))
        expected = short
        assert result == expected

# Other testing ideas
        
# Inputs
        
# Test for wrong types of inputs, if we include some error checking code 
# assert that it produces the right error message
        
# Testing large dates, or small dates (BC? 4000AD?) - is our code foolproof to 
# -400
    
# Months and dates mix up - eg setting 31 -10 instead of 10-31 for the date?
# how would we test this?
        
# "Wrong time" ie 25:00:00 or 25:61:00 or 25:61:61
# how would we assert this?
        
# what if the sum of our breaks are longer than the time interval itself?
        
