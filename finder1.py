from random import *
from abstrakterFinder import *
from gui import GUI


class Finder1(AbstrakterFinder):
    def __init__(self):
        pass

    def findePartner(self, wunschliste):
        # in wunschliste muessen w-werte uebergeben werden
        name = " "
        temp = []
        searchfile = open("file1.txt", "r")
        #for hobby in range(len(wunschliste)):
        for line in searchfile:
            check = 1
            if wunschliste[0] in line and wunschliste[1] in line and wunschliste[2] in line and wunschliste[3] in line and wunschliste[4] in line and wunschliste[5] in line:
                temp.append(line)
                check += 1
        searchfile.close()

        if check >= 1:
            i = randint(0,len(temp)-1)
            name = temp[i]
            kontaktaufnahme = temp[i]
            gui.GUI.guiAktualisieren(name, kontaktaufnahme)
        else:
            gui.GUI.guiAktualisieren(" ", " ")

    def returnPartner(self):
        # namen und Kontaktaufnahme
        pass
