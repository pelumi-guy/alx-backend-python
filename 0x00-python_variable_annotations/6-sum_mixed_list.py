#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from functools import reduce
from operator import add
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function which takes a list mxd_lst of integers
    and floats and returns their sum as a float.
    """
    return reduce(add, mxd_lst)
