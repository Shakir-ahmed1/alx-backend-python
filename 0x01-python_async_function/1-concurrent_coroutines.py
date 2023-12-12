#!/usr/bin/env python3
""" waits multiple random interval"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ a function that returns a list of waited time"""
    result = []
    for a in range(n):
        temp = await wait_random(max_delay)
        result.append(temp)
    result.sort()
    return result
