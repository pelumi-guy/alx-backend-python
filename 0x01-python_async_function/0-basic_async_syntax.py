#!/usr/bin/env python3
"""
0. The basics of async
"""


from random import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    wait_time = random() * max_delay
    await sleep(wait_time)
    return wait_time
