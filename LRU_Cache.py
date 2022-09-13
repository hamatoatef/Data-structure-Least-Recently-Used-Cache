from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cash = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key is None:
            return
        elif key in self.cash:
            value = self.cash.pop(key)
            self.cash[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key is None or value is None:
            return

        if self.capacity is None or self.capacity <= 0:
            print("The capacity can not to be", self.capacity)
            return None

        if key in self.cash:
            self.cash.pop(key)
            self.cash[key] = value

        if self.capacity == len(self.cash):
            self.cash.popitem(last=False)
            self.cash[key] = value

        else:
            self.cash[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)) # returns -1