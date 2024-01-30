#!/usr/bin/python3
"""This is the Cache module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class MRUCache"""

    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """This method inserts into the cache method"""
        if key is not None and item is not None:
            # If key already exists in cache, remove it
            if key in self.cache_data:
                self.key_order.remove(key)
            # If cache is full, remove the most recently used item
            elif len(self.key_order) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop()
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            # Add the item to the cache
            self.cache_data[key] = item
            self.key_order.append(key)

    def get(self, key):
        """ retrives from the cache method"""
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of key_order
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data.get(key)
        return None
