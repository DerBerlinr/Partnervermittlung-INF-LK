class Finder1():
    def __init__(self):
        pass

    def findePartner(self, wunschliste):
        #    1. GET DATA TO SEARCH FOR
        temp = []
        searchfile = open("file.txt", "r")
        for hobby in range(len(wunschliste[6])):
            for line in searchfile:
                if wunschliste[1] in line and wunschliste[2] in line and wunschliste[3] in line and wunschliste[4] in line and wunschliste[5] in line and wunschliste[6][hobby] in line:
                    temp.append(line)
                    searchfile.close()

        for i in len(temp):
            name = temp[i[1:6]]
            kontaktaufnahme = temp[i[7:16]]

    def returnPartner(self):
        # namen und Kontaktaufnahme
        pass
