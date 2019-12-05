from gui import GUI
from abstrakterFinder import *
from finder1 import *
from finder2 import *
from finder3 import *
from finderTroll import *



class Main:
    def __init__(self):
        self.die_gui = GUI()
        self.abstrakterFinder = AbstrakterFinder()
        self.finder1 = Finder1()
        self.finder2 = Finder2()
        self.finder3 = Finder3()

        self.aktPerson = 0

    def PersonenVonGUI(self, person):
        self.aktPerson=person
        return 0


    def speichern(self):
        variables = {}
        execfile("test.py", variables )
        print variables # globals from the someFile module



        #wichtige Methoden fuer bestimmte Schritte
