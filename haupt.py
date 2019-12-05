from gui import GUI
from abstrakterFinder import *
from finder1 import *
from finder2 import *
from finder3 import *
#from finderTroll import *



class Haupt:
    def __init__(self):
        self.abstrakterFinder = AbstrakterFinder()
        self.finder1 = Finder1()
        self.finder2 = Finder2()
        self.finder3 = Finder3()

        self.aktPerson = 0

    def personVonGUI(self, person):
        self.aktPerson=person
        return 0


    def speichern(self):
        pass



        #wichtige Methoden fuer bestimmte Schritte
