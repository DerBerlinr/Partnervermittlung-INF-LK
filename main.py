from gui import GUI
import sqlite3

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

    def speichern(self):

        connection = sqlite3.connect("company.db")
        print "opened Database succesfully"
        cursor = connection.cursor()

        # delete
        #cursor.execute("""DROP TABLE employee;""")

        sql_command = """
        CREATE TABLE singles (
        staff_number INTEGER PRIMARY KEY,
        fname VARCHAR(20),
        lname VARCHAR(30),
        gender CHAR(1),
        joining DATE,
        birth_date DATE);"""

        cursor.execute(sql_command)

        sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
            VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
        cursor.execute(sql_command)


        sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
            VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
        cursor.execute(sql_command)

        connection.commit()

        connection.close()



        #wichtige Methoden fuer bestimmte Schritte
