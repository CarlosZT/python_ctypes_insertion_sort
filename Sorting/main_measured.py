from ctypes import *
import numpy as np
import timeit
import os

#The CDLL module requires an absolute path to locate the library
path = os.getcwd() + "\\Sorting\\insort.so"
path = path.replace('\\', '/')

#Experiment cases to evaluate C and Python insertion sort implementations
input_size = 10000
RANDOM_CASE =  np.random.randint(0, input_size, input_size)
WORST_CASE = np.arange(input_size, 0, -1)
BEST_CASE = np.arange(0, input_size, 1)

#Current case selected
A = BEST_CASE

#C implementation dependences
libc = CDLL(path)
libc.insort.argtypes = [POINTER(c_int), c_int]
size = len(A)
numbers_c = (c_int * size)(*A)

#Function to call the C implementation
def insort_c():
    libc.insort(numbers_c, c_int(size))

#Function to call the Python implementation
def insort_python():
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key



def main():
    print(f'Insertion sort experiment. Input size: {input_size}')
    
    #Number of times the timeit module will execute each function to calculate the average execution time
    n_exec = 10
    
    #Experiment for C
    result_c = timeit.timeit(stmt='insort_c()', globals=globals(), number=n_exec)
    exec_time = result_c/n_exec
    print(f'Time C: {exec_time}')
    
    #Experiment for Python
    result_py = timeit.timeit(stmt='insort_python()', globals=globals(), number=n_exec)
    exec_time = result_py/n_exec
    print(f'Time Python: {exec_time}')


if __name__ == '__main__':
    main()

