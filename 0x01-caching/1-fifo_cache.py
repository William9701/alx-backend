#!/usr/bin/python3
"""This is the Cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCacheCache"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put method that saves the dict data to the cache"""
        if key is not None and item is not None:
            # Update the cache_data dictionary with the key-value pair
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the first item (FIFO) and print a discard message
                discarded_key, _ = next(iter(self.cache_data.items()))
                print(f'DISCARD: {discarded_key}')
                self.cache_data.pop(discarded_key)

    def get(self, key):
        """Get method that retrieves the value from the cache"""
        if key is not None:
            # Use .get() to handle the case when the key doesn't exist
            return self.cache_data.get(key, None)
