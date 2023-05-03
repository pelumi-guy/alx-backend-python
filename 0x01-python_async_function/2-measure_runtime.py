#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()

    return (end - start) / n
