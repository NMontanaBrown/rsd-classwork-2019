#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:04:44 2019

@author: nina

Testing case: touching edges
"""

from testing import overlap_time, time_range

def test_given_input():
        
        # large is a range of one hour length with 10 min blocks and 10 min gaps
        # short is a range of one hour length with 10 min blocks and 10 min gaps
        # but it starts 10 mins later than large
        large = time_range("2010-01-12 00:00:00", "2010-01-12 00:50:00", 3, 600) 
        short = time_range("2010-01-12 00:10:00", "2010-01-12 01:00:00", 3, 600) 
        
        result = (overlap_time(large, short))
        # there should be no overlap, should return empty tuple
        
        expected = [('2010-01-12 00:10:00', '2010-01-12 00:10:00'), ('2010-01-12 00:20:00', '2010-01-12 00:20:00'), ('2010-01-12 00:30:00', '2010-01-12 00:30:00'), ('2010-01-12 00:40:00', '2010-01-12 00:40:00'), ('2010-01-12 00:50:00', '2010-01-12 00:50:00')]
        
        assert result == expected
        