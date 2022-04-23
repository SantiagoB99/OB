# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
vector = []
for valor in range(1, 101):
    vector.append(valor)
vector.sort(reverse=True)
print("El vector en orden inverso del 1 al 100 queda: ")
print(vector)
