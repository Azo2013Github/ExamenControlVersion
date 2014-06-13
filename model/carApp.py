__author__ = 'Amine Banks'

sys.path.insert(0, '../controller')
from controller.interfaceUser import *

class car():
    def __init__(self, marca, modelo, preciodia, disponible):
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
            print("Disponoble:")

        def getMarca(self):
            return self.marca
        def getModel(self):
            return self.modelo
        def getPrecioDia(self):
            return  self.preciodia
        def getDisponible(self):
            return self.disponible

        def setDisponible(self, disponible):
            self.disponible=disponible
        def setPrecioDia(self, precio):
            self.preciodia=precio





















