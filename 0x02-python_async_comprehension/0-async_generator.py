#!/usr/bin/env python3
""" Async Generator module """
from random import uniform
import asyncio
from typing import AsyncGenerator
from time import sleep


async def async_generator() -> AsyncGenerator[float, None]:
    """ generates one value each time"""
    for i in range(10):
        asyncio.create_task(asyncio.sleep(1))
        num = uniform(0, 10)
        yield num
