#!/usr/bin/env python3
""" Async Generator """
from random import uniform
import asyncio


async def async_generator() -> None:
    """ generates one value each time"""
    for i in range(10):
        asyncio.sleep(1)
        yield uniform(0, 10)
