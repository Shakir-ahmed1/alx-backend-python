#!/usr/bin/env python3
""" a module that sleeps for a given max_daly"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """ for random length interval sleeping function """
    a = uniform(0, max_delay)
    await asyncio.sleep(a)
    return a
