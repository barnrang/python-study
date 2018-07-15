import multiprocessing as mp
import numpy as np
import time

def timer(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        return "It took " + str(t2 - t1)
    return wrapper

def test_fn(x):
    N = 10000
    a = np.zeros(N)
    for i in range(10000):
        a[i] = i * x
    return a

@timer
def single():
    N = 10000
    sum = np.zeros(N)
    for j in range(1000):
        sum += test_fn(j)

@timer
def mp_test():
    pool = mp.Pool(processes=4)
    pool_list = []
    for j in range(1000):
        pool_list.append(pool.apply_async(test_fn, (j,)))
    print('hello')

    N = 10000
    sum = np.zeros(N)
    for small_pool in pool_list:
        sum += small_pool.get()

if __name__ == "__main__":
    print(mp_test())
    print(single())
