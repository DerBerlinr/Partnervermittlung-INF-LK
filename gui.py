from Tkinter import *


class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        rahmen1=Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        self.name = ""
        self.vorname = ""
        self.geburtsdatum = ""
        self.geschlecht = ""
        self.groesse = ""
        self.figur = ""
        self.rauchverhalten = ""
        self.orientierung = ""
        self.hobby = []
        self.adresse = []
        self.telefonnummer = ""
        self.email = ""
        self.benachrichtigung = ""
        self.zahlungsart = ""
        self.iban = ""
        self.kontaktaufnahme = ""

        self.wgeschlecht = ""
        self.walter = ""
        self.wgroesse = ""
        self.wfigur = ""
        self.wrauchverhalten = ""
        self.whobby = []


        farbe = "#696969"

        abstand_x=3
        abstand_y=3

        self.la1_text=StringVar()
        self.la1_text.set("Name")
        self.la1=Label(rahmen1,textvariable=self.la1_text, width=20, bg=farbe, justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set("")
        self.en1 = Entry(rahmen1, width=8, textvariable=self.name)
        self.en1.grid(row=1,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Vorname")
        self.la2=Label(rahmen1,textvariable=self.la2_text, width=20, bg=farbe, justify=CENTER)
        self.la2.grid(row=2,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set("")
        self.en2 = Entry(rahmen1, width=8, textvariable=self.vorname)
        self.en2.grid(row=2,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Geburtsdatum")
        self.la3=Label(rahmen1,textvariable=self.la3_text, width=20, bg=farbe, justify=CENTER)
        self.la3.grid(row=3,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set("")
        self.en3 = Entry(rahmen1, width=8, textvariable=self.geburtsdatum)
        self.en3.grid(row=3,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text=StringVar()
        self.la4_text.set("Geschlecht")
        self.la4=Label(rahmen1,textvariable=self.la4_text, width=20, bg=farbe, justify=CENTER)
        self.la4.grid(row=4,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_1=Button(rahmen1,text="Maennlich", width=20, command=self.mann)
        self.bu1_1.grid(row=4,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_2=Button(rahmen1,text="Weiblich", width=20, command=self.frau)
        self.bu1_2.grid(row=4,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text=StringVar()
        self.la5_text.set("Groesse")
        self.la5=Label(rahmen1,textvariable=self.la5_text, width=20, bg=farbe, justify=CENTER)
        self.la5.grid(row=5,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.groesse = StringVar()
        self.groesse.set("")
        self.en5 = Entry(rahmen1, width=8, textvariable=self.groesse)
        self.en5.grid(row=5,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la6_text=StringVar()
        self.la6_text.set("Figur")
        self.la6=Label(rahmen1,textvariable=self.la6_text, width=20, bg=farbe, justify=CENTER)
        self.la6.grid(row=6,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_1=Button(rahmen1,text="Sportlich", width=20, command=self.sportlich)
        self.bu2_1.grid(row=6,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_2=Button(rahmen1,text="Schlank", width=20, command=self.schlank)
        self.bu2_2.grid(row=6,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_3=Button(rahmen1,text="Vollschlank", width=20, command=self.vollschlank)
        self.bu2_3.grid(row=6,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_4=Button(rahmen1,text="Dick", width=20, command=self.dick)
        self.bu2_4.grid(row=6,column=4,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la7_text=StringVar()
        self.la7_text.set("Rauchverhalten")
        self.la7=Label(rahmen1,textvariable=self.la7_text, width=20, bg=farbe, justify=CENTER)
        self.la7.grid(row=7,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_1=Button(rahmen1,text="Raucher", width=20, command=self.raucher)
        self.bu3_1.grid(row=7,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_2=Button(rahmen1,text="Nichtraucher", width=20, command=self.nichtraucher)
        self.bu3_2.grid(row=7,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la8_text=StringVar()
        self.la8_text.set("Sexuelle Orientierung")
        self.la8=Label(rahmen1,textvariable=self.la8_text, width=20, bg=farbe, justify=CENTER)
        self.la8.grid(row=8,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_1=Button(rahmen1,text="Heterosexuell", width=20, command=self.heterosexuell)
        self.bu4_1.grid(row=8,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_2=Button(rahmen1,text="Homosexuell", width=20, command=self.homosexuell)
        self.bu4_2.grid(row=8,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_3=Button(rahmen1,text="Bisexuell", width=20, command=self.bisexuell)
        self.bu4_3.grid(row=8,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la9_text=StringVar()
        self.la9_text.set("Hobbys")
        self.la9=Label(rahmen1,textvariable=self.la9_text, width=20, bg=farbe, justify=CENTER)
        self.la9.grid(row=9,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.hobby = StringVar()
        self.hobby.set("")
        self.en9 = Entry(rahmen1, width=8, textvariable=self.hobby)
        self.en9.grid(row=9,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la10_text=StringVar()
        self.la10_text.set("Adresse")
        self.la10=Label(rahmen1,textvariable=self.la10_text, width=20, bg=farbe, justify=CENTER)
        self.la10.grid(row=10,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.adresse = StringVar()
        self.adresse.set("")
        self.en10 = Entry(rahmen1, width=8, textvariable=self.adresse)
        self.en10.grid(row=10,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la11_text=StringVar()
        self.la11_text.set("Telefonnummer")
        self.la11=Label(rahmen1,textvariable=self.la11_text, width=20, bg=farbe, justify=CENTER)
        self.la11.grid(row=11,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.telefonnummer = StringVar()
        self.telefonnummer.set("")
        self.en11 = Entry(rahmen1, width=8, textvariable=self.telefonnummer)
        self.en11.grid(row=11,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text=StringVar()
        self.la12_text.set("Email")
        self.la12=Label(rahmen1,textvariable=self.la12_text, width=20, bg=farbe, justify=CENTER)
        self.la12.grid(row=12,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.email = StringVar()
        self.email.set("")
        self.en12 = Entry(rahmen1, width=8, textvariable=self.email)
        self.en12.grid(row=12,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text=StringVar()
        self.la13_text.set("Art d. Benachichtigung ueber pot. Partner")
        self.la13=Label(rahmen1,textvariable=self.la13_text, width=20, bg=farbe, justify=CENTER)
        self.la13.grid(row=13,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_1=Button(rahmen1,text="Telefon", width=20, command=self.telefon)
        self.bu5_1.grid(row=13,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_2=Button(rahmen1,text="Email", width=20, command=self.email)
        self.bu5_2.grid(row=13,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_3=Button(rahmen1,text="Post", width=20, command=self.post)
        self.bu5_3.grid(row=13,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text=StringVar()
        self.la14_text.set("Zahlungsart")
        self.la14=Label(rahmen1,textvariable=self.la14_text, width=20, bg=farbe, justify=CENTER)
        self.la14.grid(row=14,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu6_1=Button(rahmen1,text="Lastschrift", width=20, command=self.lastschrift)
        self.bu6_1.grid(row=14,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6_2=Button(rahmen1,text="Ueberweisung", width=20, command=self.ueberweisung)
        self.bu6_2.grid(row=14,column=2,sticky=E, padx=abstand_x, pady=abstand_y)


        self.la15_text=StringVar()
        self.la15_text.set("IBAN")
        self.la15=Label(rahmen1,textvariable=self.la15_text, width=20, bg=farbe, justify=CENTER)
        self.la15.grid(row=15,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.iban = StringVar()
        self.iban.set("")
        self.en15 = Entry(rahmen1, width=8, textvariable=self.iban)
        self.en15.grid(row=15,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text=StringVar()
        self.la16_text.set("Kontaktaufnahme")
        self.la16=Label(rahmen1,textvariable=self.la16_text, width=20, bg=farbe, justify=CENTER)
        self.la16.grid(row=16,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu7_1=Button(rahmen1,text="Telefon", width=20, command=self.aufnahmeTelefon)
        self.bu7_1.grid(row=16,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_2=Button(rahmen1,text="Email", width=20, command=self.aufnahmeEmail)
        self.bu7_2.grid(row=16,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_3=Button(rahmen1,text="Post", width=20, command=self.aufnahmePost)
        self.bu7_3.grid(row=16,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_4=Button(rahmen1,text="Chiffre", width=20, command=self.aufnahmeChiffre)
        self.bu7_4.grid(row=16,column=4,sticky=E, padx=abstand_x, pady=abstand_y)


        self.la17_text=StringVar()
        self.la17_text.set("Wunsch-Geschlecht")
        self.la17=Label(rahmen1,textvariable=self.la17_text, width=20, bg=farbe, justify=CENTER)
        self.la17.grid(row=17,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu8_1=Button(rahmen1,text="Maennlich", width=20, command=self.wunschmann)
        self.bu8_1.grid(row=17,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu9_2=Button(rahmen1,text="Weiblich", width=20, command=self.wunschfrau)
        self.bu9_2.grid(row=17,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text=StringVar()
        self.la18_text.set("Wunsch-Alter")
        self.la18=Label(rahmen1,textvariable=self.la18_text, width=20, bg=farbe, justify=CENTER)
        self.la18.grid(row=18,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.walter = StringVar()
        self.walter.set("")
        self.en18 = Entry(rahmen1, width=8, textvariable=self.walter)
        self.en18.grid(row=18,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text=StringVar()
        self.la19_text.set("Wunsch-Groesse")
        self.la19=Label(rahmen1,textvariable=self.la19_text, width=20, bg=farbe, justify=CENTER)
        self.la19.grid(row=19,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.wgroesse = StringVar()
        self.wgroesse.set("")
        self.en19 = Entry(rahmen1, width=8, textvariable=self.wgroesse)
        self.en19.grid(row=19,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text=StringVar()
        self.la20_text.set("Wunsch-Figur")
        self.la20=Label(rahmen1,textvariable=self.la20_text, width=20, bg=farbe, justify=CENTER)
        self.la20.grid(row=20,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_1=Button(rahmen1,text="Sportlich", width=20, command=self.wunschsportlich)
        self.bu10_1.grid(row=20,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_2=Button(rahmen1,text="Schlank", width=20, command=self.wunschschlank)
        self.bu10_2.grid(row=20,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_3=Button(rahmen1,text="Vollschlank", width=20, command=self.wunschvollschlank)
        self.bu10_3.grid(row=20,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_4=Button(rahmen1,text="Dick", width=20, command=self.wunschdick)
        self.bu10_4.grid(row=20,column=4,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la21_text=StringVar()
        self.la21_text.set("Wunsch-Rauchverhalten")
        self.la21=Label(rahmen1,textvariable=self.la21_text, width=20, bg=farbe, justify=CENTER)
        self.la21.grid(row=21,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_1=Button(rahmen1,text="Raucher", width=20, command=self.wunschraucher)
        self.bu11_1.grid(row=21,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_2=Button(rahmen1,text="Nichtraucher", width=20, command=self.wunschnichtraucher)
        self.bu11_2.grid(row=21,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la22_text=StringVar()
        self.la22_text.set("Wunsch-Hobby")
        self.la22=Label(rahmen1,textvariable=self.la22_text, width=20, bg=farbe, justify=CENTER)
        self.la22.grid(row=22,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.whobby = StringVar()
        self.whobby.set("")
        self.en22 = Entry(rahmen1, width=8, textvariable=self.whobby)
        self.en22.grid(row=22,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

    def mann(self):
        self.geschlecht = "m"

    def frau(self):
        self.geschlecht = "w"

    def sportlich(self):
        self.figur = "sportlich"

    def schlank(self):
        self.figur = "schlank"

    def vollschlank(self):
        self.figur = "vollschlank"

    def dick(self):
        self.figur = "dick"

    def raucher(self):
        self.rauchverhalten = "raucher"

    def nichtraucher(self):
        self.rauchverhalten = "nichtraucher"

    def heterosexuell(self):
        self.orientierung = "heterosexuell"

    def homosexuell(self):
        self.orientierung = "homosexuell"

    def bisexuell(self):
        self.orientierung = "bisexuell"

    def telefon(self):
        self.kontaktaufnahme = "telefon"

    def email(self):
        self.kontaktaufnahme = "email"

    def post(self):
        self.kontaktaufnahme = "post"

    def lastschrift(self):
        self.zahlungsart = "lastschrift"

    def ueberweisung(self):
        self.zahlungsart = "ueberweisung"

    def aufnahmeTelefon(self):
        self.kontaktaufnahme = "telefon"

    def aufnahmeEmail(self):
        self.kontaktaufnahme = "email"

    def aufnahmePost(self):
        self.kontaktaufnahme = "post"

    def aufnahmeChiffre(self):
        self.kontaktaufnahme = "chiffre"

    def wunschmann(self):
        self.wgeschlecht = "m"

    def wunschfrau(self):
        self.wgeschlecht = "w"

    def wunschsportlich(self):
        self.wfigur = "sportlich"

    def wunschschlank(self):
        self.wfigur = "schlank"

    def wunschvollschlank(self):
        self.wfigur = "vollschlank"

    def wunschdick(self):
        self.wfigur = "dick"

    def wunschraucher(self):
        self.wrauchverhalten = "raucher"

    def wunschnichtraucher(self):
        self.wrauchverhalten = "nichtraucher"


    def getdata(self):
        return x, y, z,

if __name__ == '__main__':
    dasFenster = GUI()
    mainloop()
