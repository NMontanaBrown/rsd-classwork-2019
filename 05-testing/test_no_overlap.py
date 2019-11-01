#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:56:10 2019

@author: nina

testing no ranges overlap
"""

from testing import overlap_time, time_range

def test_given_input():
        
        # Creating two intervals that are the same but on different days
        large = time_range("2010-01-12 00:00:00", "2010-01-12 23:50:00", 2, 600) 
        short = time_range("2010-01-13 00:00:00", "2010-01-13 23:50:00", 2, 600) 
        
        result = (overlap_time(large, short))
        # there should be no overlap, should return empty tuple
        
        expected = []
        
        assert result == expected
        
        # asserting all elements in unpacked tuple matches our requirement.