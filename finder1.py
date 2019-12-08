from random import *
from abstrakterFinder import *
from gui import *
import sqlite3


class Finder1(AbstrakterFinder):
    def __init__(self):
        pass



    def returnPartner(self):
        # namen und Kontaktaufnahme
        pass

    def findePartner(self, wunschliste):

        # TODO: Suchalgorythmus oben loeschen und testen

        conn = sqlite3.connect('test.db')
        c = conn.cursor()

        count = 0

        for i in range(6):
            if count == 0:
                a = "geschlecht"
            elif count == 1:
                a = "alter"
            elif count == 2:
                a = "groesse"
            elif count == 3:
                a = "figur"
            elif count == 4:
                a = "rauchverhalten"
            elif count == 5:
                a = "hobby"

            b = wunschliste[i-1]
            c.execute('SELECT * from benutzer WHERE ? IS ?', (a, b,))
            count += 1
            print(c.fetchall())
            for row in c.fetchall():
                print('a')
                print(row[2] + row[16])
                return row[2], row[16]

        # TODO: Name und kontaktaufnahme zurueckgeben
