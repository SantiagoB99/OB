# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países
# ordenados alfabéticamente y separados por comas.

lista = (input("Ingrese la lista de paises \n"))
lista = list(set(lista.split(", ")))
lista.sort()
print(lista)

