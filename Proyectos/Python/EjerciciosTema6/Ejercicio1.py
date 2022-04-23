# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


class Vehiculo():
    def __int__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__int__(color, ruedas, puertas)


c = Coche(120, 1500, "Rojo", 4, 4)
print("El coche es de color", c.color, "Tiene", c.ruedas, "ruedas,", c.puertas, "puertas, va a", c.velocidad,
      "km/h y tiene", c.cilindrada, " cilindradas")
