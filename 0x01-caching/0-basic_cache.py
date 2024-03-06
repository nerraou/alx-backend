#!/usr/bin/python3
""" BaseCaching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache class
    """
    def put(self, key, item):
        """
        add new item to the cache_data dictionary
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        get item with key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
