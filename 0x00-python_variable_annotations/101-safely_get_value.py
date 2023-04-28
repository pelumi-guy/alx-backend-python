#!/usr/bin/env python3
"""
11. More involved type annotations
"""
import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """annotations of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
