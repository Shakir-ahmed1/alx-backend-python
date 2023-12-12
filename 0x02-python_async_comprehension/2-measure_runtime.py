#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
from time import time

async def measure_runtime() -> int:
    """ returns the time asyncio.gather taken to run the asyncs"""
    start = time()
    await asyncio.gather(async_comprehension(),
                   async_comprehension(),
                   async_comprehension(),
                   async_comprehension())
    end = time()
    return end - start
