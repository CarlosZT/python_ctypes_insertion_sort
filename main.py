from ctypes import *

#Se importa la libreria en C
libc = CDLL("C:/Users/ChaarlyZ/OneDrive - CINVESTAV/Escritorio/Maestria/1er Cuatrimestre/Algoritmos y complejidad/Prácticas/Sorting/insort.so")

#Se definen los tipos de argumentos que recibe la función
libc.insort.argtypes = [POINTER(c_int), c_int]

#Creacion del array desde python
numbers = [22, 45, 19, 74, 82, 136, 69, 541, 14]

#Array para recibir el resultado de la libreria
sorted = []

size = len(numbers)

#Se usa la clase c_int para crear un array de C para 
# guardar el array de python (O eso entendi)
numbers_c = (c_int * size)(*numbers)

#Se llama a la funcion y se le pasan los parametros
libc.insort(numbers_c, c_int(size))

#Se itera sobre la estructura ctype para obtener el array 
#modificado por la funcion
for i in numbers_c:
  sorted.append(i)


print(f'Initial: {numbers}')
print(f'Sorted: {sorted}')
