from ctypes import *
import numpy as np
import timeit
import os

path = os.getcwd() + "\\Sorting\\insort.so"
path = path.replace('\\', '/')

RANDOM_CASE =  np.random.randint(0, 10000, 10000)
WORST_CASE = np.arange(10000, 0, -1)
BEST_CASE = np.arange(0, 10000, 1)

A = BEST_CASE

libc = CDLL(path)
libc.insort.argtypes = [POINTER(c_int), c_int]
size = len(A)
numbers_c = (c_int * size)(*A)

def insort_c():
    libc.insort(numbers_c, c_int(size))


def insort_python():
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def main():
    n_exec = 10

    result_c = timeit.timeit(stmt='insort_c()', globals=globals(), number=n_exec)
    exec_time = result_c/n_exec
    print(f'Time C: {exec_time}')

    result_py = timeit.timeit(stmt='insort_python()', globals=globals(), number=n_exec)
    exec_time = result_py/n_exec
    print(f'Time Python: {exec_time}')


if __name__ == '__main__':
    main()

