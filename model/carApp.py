__author__ = 'Amine Banks'

import os
import sys


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

        def getCar(self, disp):
            if disp == "si":
                with open("database/coche.txt", mode="r", encoding="utf-8") as file:
                    for i in file:
                        print(i)

a = car("../database/coche.txt")
print(a.getCar())

















