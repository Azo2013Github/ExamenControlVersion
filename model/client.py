__author__ = 'Amine Banks'

import re
import carApp
import alquileres
import datetime
import os.path
import sys
sys.path.insert(carApp)
sys.path.insert(alquiler)



class cliente():
    nombre=""
    apellido=""
    nif=""
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
                print("la matricula del coche: ")
                with open("fileCohes.txt", mode="w", encoding="utf-8") as file:
                    for i in file:
                        datos = i.split(";")
            #coger los indices de datos para cada Columna: y tambien incluire la clase carApp para coger la matricula del coche
                        carApp.car(datos[0], datos[1], datos[2], datos[3], datos[4])
                        if datos[1] == self.nif and carApp.car.getDisponible("matricula"):
                            print("se ha alquilado")
                            precio = carApp.car.getPrecioDia*
                        else:
                            print("no se alquilado: ")














