#!/usr/bin/python3
""" BaseCaching module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Basic cache class
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        add new item to the cache_data dictionary
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            size = len(self.cache_data)

            if size + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem()
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        get item with key
        """
        if key is None or key not in self.cache_data:
            return None

        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)

        return self.cache_data[key]
