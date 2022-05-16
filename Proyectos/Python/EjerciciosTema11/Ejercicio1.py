# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará
# de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y
# la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

con = sqlite3.connect('ejercicio.db')
cur = con.cursor()


cur.execute('''CREATE TABLE Alumnos
               (id int, nombre text, apellido text)''')


cur.execute("INSERT INTO Alumnos VALUES (1, 'Santiago', 'Berretta')")
cur.execute("INSERT INTO Alumnos VALUES (2, 'Fernando', 'Gianotti')")
cur.execute("INSERT INTO Alumnos VALUES (3, 'Franco', 'Latina')")
cur.execute("INSERT INTO Alumnos VALUES (4, 'Federico', 'Quevedo')")
cur.execute("INSERT INTO Alumnos VALUES (5, 'Valentina', 'Caldez')")
cur.execute("INSERT INTO Alumnos VALUES (6, 'Rosalba', 'Perelmult')")
cur.execute("INSERT INTO Alumnos VALUES (7, 'Celeste', 'Fernandez')")
cur.execute("INSERT INTO Alumnos VALUES (8, 'Agustina', 'Gos')")


con.commit()

for row in cur.execute('SELECT * FROM Alumnos WHERE Nombre = "Santiago"'):
    print(row)

con.close()