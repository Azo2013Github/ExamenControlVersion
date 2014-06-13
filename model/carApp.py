__author__ = 'Amine Banks'

import re

class getCar():
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
        if self.matricula == self.matricula:
            self.disponible="si"
            return self.disponible
        else:
            self.disponible=disponible
            self.marca = marca
            self.modelo = modelo
            self.preciodia=preciodia
            self.matricula=matricula
            print("No disponible:")

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

    #aanadir un nuevo coche:
        def getToFile(self):
            return str(self.matricula)+";"+str(self.marca)+";"+str(self.importe)+";"+str(self.preciodia)+";"+str(self.disponible)

    #anadir un nuevo coche
        def addCar(self):
            with open("coche.txt", mode="a", encoding="utf-8") as file:
                file.write(self.getToFile())
                print(file)


        #leer el contenido del archivo:

        def getRead(self):
            with open('coche.txt', mode='r+',encoding ='utf-8') as file:
             if re.search(file.read(),self.matricula):
                 file.write(self.getToFile())

























