# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = int(input("Ingrese el numero inicial:"))
numero_final = int(input("Ingrese el numero final:"))
resultado = []
for valor in range(numero_inicial, numero_final+1):
    if(valor%2!=0):
        resultado.append(valor)
print("Los numeros impares entre " +str(numero_inicial)+ " y " +str(numero_final)+ " es ")
print(resultado)