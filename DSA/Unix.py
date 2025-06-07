import collections
from abc import ABC, abstractmethod

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_directory = False if "." in name else True
        self.children = []
        self.extension = name.split(".")[1] if "." in name else ""
    
    def __repr__(self):
        return "{" + self.name + " }"
    

class Filter(ABC):
    def __init__ (self):
        pass

    @abstractmethod
    def apply_filter(self, file):
        pass


class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size
    
    def apply_filter(self, file):
        return file.size > self.size
    
class ExtensionFilter(Filter):
    def __init__(self, ext):
        self.ext = ext
    
    def apply_filter(self, file):
        return file.extension == self.ext    
    
class AndFilter(Filter):
    def __init__(self, *filters):
        self.filters = filters

    def apply_filter(self, file):
        return all(f.apply_filter(file) for f in self.filters)

class OrFilter(Filter):
    def __init__(self, *filters):
        self.filters = filters

    def apply_filter(self, file):
        return any(f.apply_filter(file) for f in self.filters)

class Search:
    def __init__(self):
        self.root_filter = None
        
    def set_filter(self, given_filter):
        if isinstance(given_filter, Filter):
            self.root_filter = given_filter
    
    def search_files(self, root):
        res = []
        queue = collections.deque([root])
        
        while queue:
            current = queue.popleft()
            if current.is_directory:
                queue.extend(current.children)
            elif self.root_filter is None or self.root_filter.apply_filter(current):
                res.append(current)
        
        return res
    

dir_p = File("root", 0)
file1 = File("a.txt", 50)
file2 = File("b.jpg", 150)
file3 = File("c.txt", 200)
dir1 = File("dir1", 0)
dir1.children.extend([file1, file2])
dir_p.children.extend([dir1, file3])

# Filters
size_filter = SizeFilter(100)
ext_filter = ExtensionFilter("txt")

# Composite: (size > 100 OR extension == 'txt')
composite_filter = OrFilter(size_filter, ext_filter)

# Search
search = Search()
search.set_filter(composite_filter)

results = search.search_files(dir_p)
print(results)  # Expected: [{a.txt }, {b.jpg }, {c.txt }]
                
        
    
    
        



    
    
        