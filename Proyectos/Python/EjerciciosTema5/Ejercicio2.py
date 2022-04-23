# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(numero):
    resultado=True
    if(numero==0 or numero==1):
        resultado = False
    for valor in range(2, numero):
        if (numero % valor == 0):
            resultado=False
            break
    return resultado

numero = int(input("Ingrese el numero a evaluar "))
if(esPrimo(numero)):print("El numero es primo")
else:print("El numero NO es primo")
