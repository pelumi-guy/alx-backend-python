#!/usr/bin/env python3
"""
0. Async Generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    A coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        random_number = random.uniform(0, 10)
        yield random_number
        await asyncio.sleep(1)
