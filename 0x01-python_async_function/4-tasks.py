#!/usr/bin/env python3
""" excutes task_wait_random function multiple times"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ a function that returns a list of time intervals"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    result = []
    for future in asyncio.as_completed(tasks):
        temp = await future
        result.append(temp)
    return result
