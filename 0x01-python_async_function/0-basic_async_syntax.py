#!/usr/bin/env python3
""" a module that sleeps for a given max_daly"""
import asyncio
from random import uniform
from time import sleep


async def wait_random(max_delay: int = 10) -> float:
    """ for random length interval sleeping function """
    a = uniform(0, max_delay)
    sleep(a)
    return a
