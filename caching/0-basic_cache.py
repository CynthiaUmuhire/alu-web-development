#!/usr/bin/python3
""" BaseCaching module
"""


class BasicCache():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ check if the key or item is none
        """
        if key is None or item is None:
            return
        """ Add an item in the cache
        """
        self.cache_data[key] = item

    def get(self, key):
        """ Check if an item or the key is none
        """
        if key is None or key is not self.cache_data:
            return None
        """ Get an item by key
        """
        return self.cache_data.get(key)



