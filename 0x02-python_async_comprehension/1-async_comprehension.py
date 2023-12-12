#!/usr/bin/env python3
""" async Comprehension in python """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """ async comprehension that returns list of floats"""
    return [a async for a in async_generator()]
