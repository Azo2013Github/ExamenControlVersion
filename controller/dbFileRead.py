__author__ = 'Amine Banks'

sys.path.insert(0,"../interfaceUser")

from controller.interfaceUser import *

class DBController():
    def __init__(self, pathToDb="../database/coche.txt"):
        self.pathToDb = pathToDb
    def writeFile(self):
        with open(self.pathToDb, mode="r", encoding="utf-8") as f:
            for line in f:
                datos = line.split(";")
                print(f)
                print("Succes full", f)
                return f






