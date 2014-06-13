__author__ = 'Amine Banks'

def __init__(self, nombre, apellido, nif):
        self.nombre = nombre
        self.apellido=apellido
        self.nif=nif
        def getNombre(self):
            return self.nombre
        def getApellido(self):
            return self.appellido
        def getnif(self):
            return  self.nif
        def setNombre(self, nombre):
            self.nombre = nombre
        def setApellido(self, apellido):
            self.appellido=apellido
        def setNif(self, nif):
            self.nif = nif
        def cocheAquiladoCliente(self):
            with open("fileCohes.txt", mode="a", encoding="utf-8") as file:



