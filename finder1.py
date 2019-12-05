from random import *
from abstrakterFinder import *


class Finder1(AbstrakterFinder):
    def __init__(self):
        pass

    def findePartner(self, wunschliste):
        # in wunschliste muessen w-werte uebergeben werden
        name = " "
        temp = []
        searchfile = open("file1.txt", "r")
        for hobby in range(len(wunschliste)):
            for line in searchfile:
                if wunschliste[0] in line and wunschliste[1] in line and wunschliste[2] in line and wunschliste[3] in line and wunschliste[4] in line and wunschliste[5][hobby] in line:
                    temp.append(line)
                    searchfile.close()

        laengeListe = len(temp)
        i = randint(0,laengeListe-1)
        name = temp[i]
        #name = temp[i[0:6]]
        kontaktaufnahme = temp[i[7:16]]
        return name, kontaktaufnahme

    def returnPartner(self):
        # namen und Kontaktaufnahme
        pass
