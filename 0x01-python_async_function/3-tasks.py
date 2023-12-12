#!/usr/bin/env python3
""" creates a task instances """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns a task instance of wait_random function """
    return asyncio.Task(wait_random(max_delay))

