__author__ = 'Amine Banks'


class car():
    matricula=""
    marca=""
    modelo=""
    preciodia=""
    disponible=""
    def __init__(self, matricula,marca, modelo, preciodia, disponible):
        self.matricula=matricula
        self.marca = marca
        self.modelo=modelo
        self.preciodia=preciodia
        self.disponible=disponible
        if disponible == "no":
            self.disponible="no"
        else:
            self.disponible=disponible
            self.marca = marca
            self.modelo = modelo
            self.preciodia=preciodia
            self.matricula=matricula
            print("Disponoble:")

        def getMarca(self):
            return self.marca
        def getModel(self):
            return self.modelo
        def getPrecioDia(self):
            return  self.preciodia
        def getDisponible(self):
            return self.disponible
        def getMatricula(self):
            return self.matricula

        def setDisponible(self, disponible):
            self.disponible=disponible
        def setPrecioDia(self, precio):
            self.preciodia=precio
        def setMarca(self, marca):
            self.marca=marca
        def setModel(self, modelo):
            self.modelo=modelo
        def setMatricula(self, matricula):
            self.matricula=matricula






















