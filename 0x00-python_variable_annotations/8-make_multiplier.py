#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.
    """
    def float_multiplier(x: float) -> float:
        return x * multiplier

    return float_multiplier
