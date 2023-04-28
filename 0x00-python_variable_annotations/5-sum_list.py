#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from functools import reduce
from operator import add
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function which takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    return reduce(add, input_list)
