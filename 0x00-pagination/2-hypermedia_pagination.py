#!/usr/bin/env python3
"""
Server class
"""
from typing import Tuple, List
from math import ceil
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return start index and end index of a page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return page
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        [start, end] = index_range(page, page_size)

        self.dataset()
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return page with extra data
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        [start, end] = index_range(page, page_size)

        dataset = self.dataset()

        data = dataset[start:end]

        total_pages = ceil(len(dataset) / page_size)

        prev_page = None if page == 1 else page - 1
        next_page = None if page > total_pages else page + 1

        return {
            "page_size": len(data),
            "page": page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
            "data": data
        }
