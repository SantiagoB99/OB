# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra
# función que calcule el área de un círculo recibiendo el radio del mismo.
import math


def area_triangulo(base, altura):
    print("El area del triangulo de base ",base," y altura ", altura, " es")
    return (base * altura) / 2


def area_circulo(radio):
    print("El area del circulo de radio ",radio," es ")
    return math.pi * radio * radio


print(area_triangulo(int(input("Ingrese la base del triangulo ")), int(input("Ingrese la altura del triangulo "))))
print(area_circulo(int(input("Ingrese el radio del circulo "))))
