from Tkinter import *
from gui import *


class GUI_anmelden(Tk):
    def __init__(self):
        Tk.__init__(self)
        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#696969"

        abstand_x=3
        abstand_y=3

        groesse = 20

        self.la1_text=StringVar()
        self.la1_text.set("Benutzername:")
        self.la1=Label(rahmen1,textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Passwort:")
        self.la2=Label(rahmen1,textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Account registrieren/anmelden:")
        self.la3=Label(rahmen1,textvariable=self.la3_text, width=30, bg="red", justify=CENTER)
        self.la3.grid(row=0,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.benutzername = StringVar()
        self.benutzername.set("")
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.benutzername)
        self.en1.grid(row=1,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.passwort = StringVar()
        self.passwort.set("")
        self.en2 = Entry(rahmen1, width=groesse, textvariable=self.passwort)
        self.en2.grid(row=2,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_1=Button(rahmen1,text="anmelden/registrieren", width=groesse, command=self.fertig)
        self.bu1_1.grid(row=3,column=1,sticky=E, padx=abstand_x, pady=abstand_y)






    def fertig(self):
        temp = []
        listeDaten = []
        check=0
        searchfile = open("nutzer.txt", "r")
        print "suche",self.benutzername.get(), self.passwort.get()
        for line in searchfile:
            if self.benutzername.get() in line and self.passwort.get() in line:
                temp.append(line)
                check=1
                print temp, "gefunden"
            else:
                for line in searchfile:
                    listeDaten.append(line)
                    print "Daten in Liste"
        searchfile.close()
        print check
        if check == 0:
            writefile = open("nutzer.txt", "w+")
            print "in Bedingung"
            for line in writefile:
                print "in Schleife"
                if "#" in line:
                    print "schreibe"
                    print listeDaten
                    for i in listeDaten:
                        writefile.write(listeDaten[i])
            writefile.close()





        dasFenster.destroy()
        die_gui = GUI()




if __name__ == '__main__':
    dasFenster = GUI_anmelden()
    mainloop()
