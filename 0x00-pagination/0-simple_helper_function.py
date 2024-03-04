#!/usr/bin/env python3
"""
simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return start index and end index of a page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
