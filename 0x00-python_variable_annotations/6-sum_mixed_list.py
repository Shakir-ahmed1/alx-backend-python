#!/usr/bin/env python3
""" mixed values of int and flaot in list """
from typing import Union, List

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns sum of the given numbers"""
    result = 0
    for value in mxd_list:
        result += value
    return result
