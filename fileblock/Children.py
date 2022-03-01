from random import random


class Children(list):
    
    @property
    def paths(self):
        return [child.abspath for child in self]
    
    @property
    def shuffle(self):
        res = self.copy()
        index = []
        le = res.__len__()
        for i in range(1, le+1):
            idx = int(random() * (le - i))
            index.append(idx)
            res[idx], res[le - i] = res[le - i], res[idx]
        return res

    def __add__(self, x):
        return Children(super().__add__(x))

if __name__  == "__main__":

    c = Children()
    x = c + Children()
    