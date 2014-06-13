__author__ = 'Amine Banks'

import datetime
import os
import sys
sys.path.insert(1, '')


class alquiler:
    matricula=""
    nifCliente=""
    dateAlquilado=""
    fechaReturnar=""
    importe=""
    operationCompleta=False
    def __init__(self,matricula,nifCliente, fechaAlquilado,fechaReturnar,importe, operationCompleta):
        self.matricula=matricula
        self.nifCliente=nifCliente
        self.fechaAlquilado=fechaAlquilado
        self.fechaReturnar=fechaReturnar
        self.importe=importe
        self.operationCompleta=operationCompleta



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

    def setCompletada(self,operationCompleta):
         self.operationCompleta=operationCompleta





