#!/usr/bin/env python3
""" Complex types -functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a function that returns a function """
    def mul(val: float) -> float:
        return val * multiplier
    return mul
