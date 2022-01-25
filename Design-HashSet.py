class MyHashSet:

    def __init__(self):
        self.hash_set = [None] * 1000
        

    def add(self, key: int) -> None:
        first_key = key % 1000
        second_key = key // 1000
        if self.hash_set[first_key] == None:
            self.hash_set[first_key] = [False] * 1001
        self.hash_set[first_key][second_key] = True
        

    def remove(self, key: int) -> None:
        first_key = key % 1000
        second_key = key // 1000
        if self.hash_set[first_key] != None:
            if self.hash_set[first_key][second_key] == True:
                self.hash_set[first_key][second_key] = False
        

    def contains(self, key: int) -> bool:
        first_key = key % 1000
        second_key = key // 1000
        if self.hash_set[first_key] != None:
            if(self.hash_set[first_key][second_key] == True):
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
