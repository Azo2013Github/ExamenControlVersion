__author__ = 'Amine Banks'


import os
import sys
import re
import os.path



class getAquiler:
    matricula=""
    nifCliente=""
    dateAlquilado=""
    fechaReturnar=""
    importe=""

    def __init__(self,matricula,nifCliente, fechaAlquilado,fechaReturnar,importe):
        self.matricula=matricula
        self.nifCliente=nifCliente
        self.fechaAlquilado=fechaAlquilado
        self.fechaReturnar=fechaReturnar
        self.importe=importe

    def getMatricula(self):
        return self.matricula

    def getNif(self):
        return self.nif

    def getFecha_alquiler(self):
        return self.fechaAlquilado

    def getFechaRetour(self):
        return self.fechaReturnar

    def getImporte(self):
        return self.importe

    def getOperationCompleta(self):
        return self.operationCompleta

    def setMatricula(self,matricula):
         self.matricula=matricula

    def setNif(self,nif):
         self.nif=nif

    def setFecha_alquiler(self,fecha_alquiler):
         self.fecha_alquiler=fecha_alquiler

    def setFecha_debolucion(self,fecha_debolucion):
         self.fecha_debolucion=fecha_debolucion

    def setImporte(self,importe):
         self.importe=importe



    def getToString(self):
        return str(self.matricula)+";"+str(self.nifCliente)+";"+str(self.fechaAlquilado)+";"+str(self.fechaReturnar)+";"+str(self.importe)

    def getWrite(self):
        with open("alquiler.txt", mode="a", encoding="utf-8") as file:
            file.write(self.getString())



    #conocer los ingresos totales obtenidos en un periodo de fechas:
            def getIngress(self):
                n= input("Ingreso total: ")





a = getAquiler()
print(a.getWrite())







