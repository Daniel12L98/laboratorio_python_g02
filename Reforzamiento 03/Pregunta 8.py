class Persona:
    def __init__(self):
        self.datos = {}


    def pedir_nombre_apellido (self):
        nombre = input("Ingresar nombre: ")
        apellido = input("Ingresar apellido: ")
        self.datos['nombre'] = nombre
        self.datos['apellido'] = apellido


    def pedir_edad(self):
        edad = input("Ingresar edad: ")
        self.datos['edad'] = edad


    def resultados(self):
        print("El diccionario es: {}".format(self.datos))
        print("Nombre:", self.datos.get('nombre'))
        print("Apellido:", self.datos.get('apellido'))
        print("Edad:", self.datos.get('edad'))


persona = Persona()
persona.pedir_nombre_apellido()
persona.pedir_edad()
persona.resultados()
