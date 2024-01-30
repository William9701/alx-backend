#!/usr/bin/python3
"""This is the Cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class LRUCache"""

    def __init__(self):
        super().__init__()
        self.order_tracker = OrderedDict()

    def put(self, key, item):
        """Put method that saves the dict data to the cache"""
        if key is not None and item is not None:
            # Update the cache_data dictionary with the key-value pair
            self.cache_data[key] = item
            # Update the order tracker with the current key
            self.order_tracker.pop(key, None)
            self.order_tracker[key] = True

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Retrieve and remove the least recently used item (LRU)
                # from the cache_data
                lru_key, _ = self.order_tracker.popitem(last=False)
                print(f'DISCARD: {lru_key}')
                self.cache_data.pop(lru_key)

    def get(self, key):
        """Get method that retrieves the value from the cache"""
        if key is not None:
            # Use .get() to handle the case when the key doesn't exist
            value = self.cache_data.get(key, None)
            if value is not None:
                # Update the order tracker with the current key
                self.order_tracker.pop(key, None)
                self.order_tracker[key] = True
            return value
