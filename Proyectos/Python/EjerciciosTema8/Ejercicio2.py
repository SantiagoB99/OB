# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto
# de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    ruedas = 0
    puertas = 0

    def __init__(self, ruedas, puertas):
        self.ruedas=ruedas
        self.puertas=puertas

    def getPuertas(self):
        return self.puertas

    def getRuedas(self):
        return self.ruedas

v = Vehiculo(4, 4)

f = open('archivo.bin', 'wb')
pickle.dump(v,f)
f.close()

f = open('archivo.bin', 'rb')
v1=pickle.load(f)
f.close()

print("El coche tiene", v1.getRuedas(), "ruedas y 4", v1.getPuertas(), "puertas")