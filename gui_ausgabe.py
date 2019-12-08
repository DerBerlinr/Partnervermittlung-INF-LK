from tkinter import *
from gui import *


class GUI_ausgabe(Tk):
    def __init__(self, name, kontaktaufnahme):
        Tk.__init__(self)
        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#696969"

        abstand_x=3
        abstand_y=3

        groesse = 20

        self.la1_text=StringVar()
        self.la1_text.set("Name:")
        self.la1=Label(rahmen1,textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Kontaktaufnahme:")
        self.la2=Label(rahmen1,textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Treffer!")
        self.la3=Label(rahmen1,textvariable=self.la3_text, width=50, bg="red", justify=CENTER)
        self.la3.grid(row=0,column=0,columnspan=3)

        self.la1_text=StringVar()
        self.la1_text.set(name)
        self.la1=Label(rahmen1,textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set(kontaktaufnahme)
        self.la2=Label(rahmen1,textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_1=Button(rahmen1,text="zurück zur Partnervermittlung", width=groesse, command=self.zurueck)
        self.bu1_1.grid(row=3,column=1,sticky=E, padx=abstand_x, pady=abstand_y)


    def zurueck(self):
        dasFenster.destroy()
        die_gui = GUI()







if __name__ == '__main__':
    dasFenster = GUI_ausgabe("a", "b")
    mainloop()
