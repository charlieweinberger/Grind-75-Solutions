# https://leetcode.com/problems/lru-cache/

class LRUCache:

    """ Slow solution (not sure how) """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUCache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.order:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.LRUCache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.order.remove(key)
            self.LRUCache[key] = value
        elif len(self.order) >= self.capacity:
            keyToDelete = self.order[0]
            del self.order[0]
            del self.LRUCache[keyToDelete]
        self.order.append(key)
        self.LRUCache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)