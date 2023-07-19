import heapq
import time
import math

class CacheItem:
    def __init__(self, key, value, weight, last_accessed_time):
        self.key = key
        self.value = value
        self.weight = weight
        self.last_accessed_time = last_accessed_time

    def __lt__(self, other):
        return self.score() < other.score()

    def score(self):
        current_time = time.time()
        return self.weight / (math.log(current_time - self.last_accessed_time + 1) + 1)

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.priority_queue = []

    def get(self, key):
        if key in self.cache:
            cache_item = self.cache[key]
            self.update_last_accessed_time(cache_item)
            return cache_item.value
        else:
            return -1

    def put(self, key, value, weight):
        if key in self.cache:
            cache_item = self.cache[key]
            cache_item.value = value
            cache_item.weight = weight
            self.update_last_accessed_time(cache_item)
        else:
            if len(self.cache) >= self.capacity:
                self.evict_least_scored_item()
            current_time = time.time()
            cache_item = CacheItem(key, value, weight, current_time)
            self.cache[key] = cache_item
            heapq.heappush(self.priority_queue, cache_item)

    def update_last_accessed_time(self, cache_item):
        current_time = time.time()
        cache_item.last_accessed_time = current_time
        heapq.heapify(self.priority_queue)

    def evict_least_scored_item(self):
        cache_item = heapq.heappop(self.priority_queue)
        del self.cache[cache_item.key]

# Example usage
cache = Cache(3)

cache.put('key1', 'value1', 1)
cache.put('key2', 'value2', 2)
cache.put('key3', 'value3', 3)
cache.put('key4', 'value4', 4)

print(cache.get('key1'))  # Output: -1
print(cache.get('key2'))  # Output: 'value2'
print(cache.get('key3'))  # Output: 'value3'
print(cache.get('key4'))  # Output: 'value4'

cache.put('key5', 'value5', 5)

print(cache.get('key2'))  # Output: -1
print(cache.get('key3'))  # Output: 'value3'
print(cache.get('key4'))  # Output: 'value4'
print(cache.get('key5'))  # Output: 'value5'

# space complexity: O(n) // n is the number of items in the cache

# 'put' function has a time complexity of O(log n), 
# where n represents the number of items in the priority queue.
# However, since the number of items in the priority queue is 
# limited to the cache capacity (a constant), the overall time complexity 
# of the put function remains logarithmic.