#!/usr/bin/python3
"""This is the Cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCache"""

    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """Put method that saves the dict data to the cache"""
        if key is not None and item is not None:
            # Update the cache_data dictionary with the key-value pair
            self.cache_data[key] = item
            # Add the key to the key_order list
            self.key_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the last inserted key (LIFO)
                discarded_key = self.key_order[-2]
                print(f'DISCARD: {discarded_key}')
                # Remove the discarded_key from both the cache_data and
                # key_order
                self.cache_data.pop(discarded_key)
                self.key_order.remove(discarded_key)

    def get(self, key):
        """Get method that retrieves the value from the cache"""
        if key is not None:
            # Use .get() to handle the case when the key doesn't exist
            return self.cache_data.get(key, None)
