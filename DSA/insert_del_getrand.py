from random import choice
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.dict = defaultdict(set)  # Use set for indices to handle duplicates
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict and self.dict[val]: 
            return False
        self.dict[val].add(len(self.list))  # Store the index of the value
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict or not self.dict[val]:
            return False
        
        remove_index = self.dict[val].pop()  # Get an index of the value to remove
        last_val = self.list[-1]
        
        if remove_index != len(self.list) - 1:
            # Swap the value to remove with the last element
            self.list[remove_index] = last_val
            self.dict[last_val].remove(len(self.list) - 1)
            self.dict[last_val].add(remove_index)
        
        # Remove the last element
        self.list.pop()

        if not self.dict[val]:
            del self.dict[val]

        return True    

    def getRandom(self) -> int:
        return choice(self.list)
    
obj = RandomizedSet()
print(obj.insert(1))  # True (first insertion)
print(obj.insert(1))  # False (duplicate)
print(obj.insert(2))  # True (new insertion)
print(obj.remove(1))  # True (removes one occurrence of 1)
print(obj.getRandom())  # Randomly 1 or 2


## B TREE DFS