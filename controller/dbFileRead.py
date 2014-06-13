__author__ = 'Amine Banks'

import os
import sys

sys.path.insert(0,"../interfaceUser")

from interfaceUser import *

class DBController():
    def __init__(self, pathToDb="../database/coche.txt"):
        self.pathToDb = pathToDb

    def writeFile(self):
        with open(self.pathToDb, mode="r", encoding="utf-8") as f:
            for line in f:
                print("Succes full", f)






