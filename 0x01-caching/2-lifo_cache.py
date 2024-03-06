#!/usr/bin/python3
""" BaseCaching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Basic cache class
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.keys_stack = []

    def put(self, key, item):
        """
        add new item to the cache_data dictionary
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        size = len(self.cache_data)

        if size > BaseCaching.MAX_ITEMS:
            last_key = self.keys_stack[-1]
            self.keys_stack.pop()
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)

        self.keys_stack.append(key)

    def get(self, key):
        """
        get item with key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
