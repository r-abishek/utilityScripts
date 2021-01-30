import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
# print(arr)
data = arr.tolist()
# print(data)
data[:5]


# Solution Without Paralleization
'''
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    
    trial = 0
    for i in list(range(5000)):
        trial += 1
    return count

results = []
start_time = time()
for row in data:
    results.append(howmany_within_range(row, minimum=4, maximum=8))
end_time = time()

print(results[:10])
print("--- %s seconds ---" % (end_time - start_time))
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
'''

'''

# Parallelizing using Pool.apply()

import multiprocessing as mp

# Step 1: Init multiprocessing.Pool()
# pool = mp.Pool(mp.cpu_count())
pool = mp.Pool(10)

# Step 2: `pool.apply` the `howmany_within_range()`
results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

# Step 3: Don't forget to close
pool.close()    

print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

'''

# '''

# Parallelizing using Pool.map()

import multiprocessing as mp

# Redefine, with only 1 mandatory argument.
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    
    trial = 0
    for i in list(range(5000)):
        trial += 1
    
    return count

pool = mp.Pool(mp.cpu_count())
# pool = mp.Pool(10)

start_time = time()
# results = pool.map(howmany_within_range_rowonly, [row for row in data])
results = pool.map(howmany_within_range_rowonly, [data[i] for i in list(range(len(data)))])
end_time = time()

pool.close()

print(results[:10])
print("--- %s seconds ---" % (end_time - start_time))
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

# '''













