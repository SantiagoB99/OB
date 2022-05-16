#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
# de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos
# obtenidos mediante reduce.

# importing functools for reduce()
from functools import reduce

def impares(x):
    return x % 2 != 0

def suma(a,b):
    return a+b

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = list(filter(impares, lista))
print("Numeros impares", numeros_impares)
print("La suma de los numeros impares es: ")
print(reduce(suma, numeros_impares))

