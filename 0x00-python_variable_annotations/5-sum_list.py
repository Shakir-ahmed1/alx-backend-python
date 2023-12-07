#!/usr/bin/env python3
""" list of floats annotation """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum of list of floats """
    result = 0
    for value in input_list:
        result += value
    return result
