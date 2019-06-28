import random
import time
import copy
from statistics import median
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
A = random_int_list(-100,100,1000000)
B = random_int_list(-100,100,100000)



start=copy.deepcopy(time.time())

print(median(A+B))


        
time = time.time() - start

print(time)
