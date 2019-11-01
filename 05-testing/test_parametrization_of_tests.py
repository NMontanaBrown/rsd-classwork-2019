#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:26:40 2019

@author: nina
Parametrizing tests
"""

import pytest 
from testing import overlap_time, time_range

# Parametrizing the values through pytest
# In the inverted commas you get the arguments to be used
# in the tuple you should encounter the pairs of items you want to test

# The example below is the no_overlap case where an empty tuple should be returned.
@pytest.mark.parametrize("large, small, expected", [(time_range("2010-01-12 00:00:00", "2010-01-12 23:50:00", 2, 600),
                                                     time_range("2010-01-13 00:00:00", "2010-01-13 23:50:00", 2, 600), 
                                                     [])] )

# defining the test
# it will run for all the tuple groups defined above
def test_eval(large, small, expected):
    assert (overlap_time(large, small)) == expected