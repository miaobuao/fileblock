import time

from fileblock import Children

a = Children()

b = Children(list(range(100)))
st = time.time()
for i in range(1000000):
    a += b
print(time.time() - st)
