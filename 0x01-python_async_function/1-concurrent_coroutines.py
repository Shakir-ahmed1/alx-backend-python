#!/usr/bin/env python3
""" waits multiple random interval"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ a function that returns a list of waited time"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    result = []
    for future in asyncio.as_completed(tasks):
        temp = await future
        result.append(temp)
    return result
