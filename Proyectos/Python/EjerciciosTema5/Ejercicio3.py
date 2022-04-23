# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(anio):
    return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))


anio = int(input("Ingrese el anio a evaluar "))
if esBisiesto(anio):
    print("El anio es bisiesto")
else:
    print("El anio NO es bisiesto")
