#!/usr/bin/env python3
""" string and int/float to tuple annotation """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a function that returns tuple of string and number"""
    return (k, v ** 2)
