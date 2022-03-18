class LRUCache:

    def __init__(self, capacity: int):
        self.dict_ = dict()
        self.capacity = capacity
        
        
    def get(self, key: int) -> int:
        if key not in self.dict_ :
            return -1
        val = self.dict_.pop(key) # Remove it before inserting  for LRU Key
        self.dict_[key] = val
        return val
            

    def put(self, key: int, value: int) -> None:
        if key  in self.dict_:
            self.dict_.pop(key)
        elif len(self.dict_) == self.capacity:
            del self.dict_[next(iter(self.dict_))]
        self.dict_[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
lru = dict()
lru["a"] = 0
lru["b"] = 1
lru["c"] = 2
lru["d"] = 3
for i in range(4):
    item = lru[next(iter(lru))]
    print(item)
    del lru[next(iter(lru))]
'''    