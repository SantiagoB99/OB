# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como
# atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrarNota(self):
        print(self.nota)

    def mostrarNombre(self):
        print(self.nombre)

    def resultado(self):
        print("El alumno obtuvo un ", self.nota)
        if self.nota >= 4:
           print("Por lo tanto aprobó")
        else:
            print("Por lo tanto no aprobó")

a = Alumno("Santiago", 4)
a.resultado()