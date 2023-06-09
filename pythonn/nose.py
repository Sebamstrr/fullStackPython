class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

class RegistroAsistencia:
    def __init__(self, curso):
        self.curso = curso
        self.asistencias = {}
    
    def marcar_asistencia(self, estudiante):
        if estudiante in self.curso.estudiantes:
            self.asistencias[estudiante.nombre] = True
            print(f"Asistencia registrada para {estudiante.nombre}")
        else:
            print(f"El estudiante {estudiante.nombre} no está inscrito en el curso")


def mostrar_menu():
    print("-----menu-----")
    print("|| OPCIÓN 1: estudiante1  ||")
    print("|| OPCIÓN 2: estudiante2  ||")
    print("|| OPCIÓN 3: estudiante3  ||")
    print("|| OPCIÓN 4: estudiante4  ||")
    print("|| OPCIÓN 0: estudiante5  ||")
    print("*--------------------------*")


estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("María")
estudiante3 = Estudiante("Carlos")
estudiante4 = Estudiante("bryant")
estudiante5 = Estudiante("mati")

curso = Curso("Programación")

curso.agregar_estudiante(estudiante1)
curso.agregar_estudiante(estudiante2)
curso.agregar_estudiante(estudiante3)
curso.agregar_estudiante(estudiante4)
curso.agregar_estudiante(estudiante5)

registro_asistencia = RegistroAsistencia(curso)

registro_asistencia.marcar_asistencia(estudiante1)
registro_asistencia.marcar_asistencia(estudiante2)
registro_asistencia.marcar_asistencia(estudiante3)
registro_asistencia.marcar_asistencia(estudiante4)
registro_asistencia.marcar_asistencia(estudiante5)