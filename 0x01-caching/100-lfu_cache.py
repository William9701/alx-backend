#!/usr/bin/python3
"""This is the Cache module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This is the LFUCacche"""

    def __init__(self):
        """ This is the init method"""
        super().__init__()
        self.key_order = []
        self.key_frequency = {}

    def put(self, key, item):
        """This is the put method used to insert data into the cache"""
        if key is not None and item is not None:
            # If key already exists in cache, remove it
            if key in self.cache_data:
                self.key_order.remove(key)
            # If cache is full, remove the least frequently used item
            elif len(self.key_order) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.key_frequency.values())
                least_freq_keys = [k for k, v in self.key_frequency.items()
                                   if v == least_freq]
                if len(least_freq_keys) > 1:
                    # If there is more than one least frequently used
                    # item, use LRU
                    for k in self.key_order:
                        if k in least_freq_keys:
                            discarded_key = k
                            break
                else:
                    discarded_key = least_freq_keys[0]
                self.key_order.remove(discarded_key)
                del self.cache_data[discarded_key]
                del self.key_frequency[discarded_key]
                print(f"DISCARD: {discarded_key}")
            # Add the item to the cache
            self.cache_data[key] = item
            self.key_order.append(key)
            self.key_frequency[key] = self.key_frequency.get(key, 0) + 1

    def get(self, key):
        """This is the get method used to get the data from the cache"""
        if key is not None and key in self.cache_data:
            # Increase the frequency of the accessed key
            self.key_frequency[key] += 1
            return self.cache_data.get(key)
        return None
