#!/usr/bin/env python3
""" Async Generator module """
from random import uniform
import asyncio


async def async_generator() -> None:
    """ generates one value each time"""
    for i in range(10):
        asyncio.sleep(1)
        num = uniform(0, 10)
        yield num
