#!/usr/bin/env python3
""" Duck typing an iterable object """
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ given function """
    return [(i, len(i)) for i in lst]
