class Finder1():
    def __init__(self):
        pass

    def findePartner(self):

        #    1. GET DATA TO SEARCH FOR

        searchfile = open("file.txt", "r")
        for line in searchfile:
            if "searchphrase" in line:
                print line
            searchfile.close()

    def returnPartner(self):
        pass
