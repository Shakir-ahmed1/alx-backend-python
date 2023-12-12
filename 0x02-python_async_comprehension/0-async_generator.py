#!/usr/bin/env python3
""" Async Generator module """
from random import uniform
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generates one value each time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
