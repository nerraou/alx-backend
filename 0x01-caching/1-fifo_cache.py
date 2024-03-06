#!/usr/bin/python3
""" BaseCaching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic cache class
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """
        add new item to the cache_data dictionary
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.keys_queue.append(key)

        size = len(self.cache_data)

        if size > BaseCaching.MAX_ITEMS:
            first_key = self.keys_queue[0]
            self.keys_queue.pop(0)
            self.cache_data.pop(first_key)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        get item with key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
