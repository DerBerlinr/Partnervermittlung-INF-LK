from random import *
from abstrakterFinder import *


class Finder2(AbstrakterFinder):
    def __init__(self):
        pass

    def findePartner(self, wunschliste):
        # in wunschliste muessen w-werte uebergeben werden
        temp = []
        searchfile = open("file.txt", "r")
        for hobby in range(len(wunschliste[6])):
            for line in searchfile:
                if wunschliste[1] in line and wunschliste[2] in line and wunschliste[3] in line and wunschliste[4] in line and wunschliste[5] in line and wunschliste[6][hobby] in line:
                    temp.append(line)
                    searchfile.close()

        laengeListe = len(temp)
        i = randint(0,laengeListe)
        name = temp[i[1:6]]
        kontaktaufnahme = temp[i[7:16]]
        return name, kontaktaufnahme

    def returnPartner(self):
        # namen und Kontaktaufnahme
        pass

        temp[4]
        temp[i[1:6]]
