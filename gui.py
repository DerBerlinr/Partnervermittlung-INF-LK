from Tkinter import *


class GUI:
    def __init__(self):
        self.fenster=Tk()
        self.fenster.geometry("700x700")
        self.fenster.resizable(width="false",height="false")
        self.fenster.title("Partnervermittlung")


        rahmen1=Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()


        self.name = "" E1 +
        self.vorname = "" E2 +
        self.geburtsdatum = "" E3 +
        self.geschlecht = "" B4 +
        self.groesse = "" E5 +
        self.figur = "" B6 +
        self.rauchverhalten = "" B7 +
        self.orientierung = "" B8 +
        self.hobby = [] E9 +
        self.adresse = [] E10 +
        self.telefonnummer = "" E11 +
        self.email = "" E12 +
        self.benachrichtigung = "" B13 +
        self.zahlungsart = "" B14 +
        self.iban = "" E15 +
        self.kontaktaufnahme = "" B16 +

        self.wgeschlecht = "" B17 +
        self.walter = "" E18 +
        self.wgroesse = "" E19 +
        self.wfigur = "" B20 +
        self.wrauchverhalten = "" B21 +
        self.whobby = [] E22 +


        abstand_x=3
        abstand_y=3

        self.la1_text=StringVar()
        self.la1_text.set("Name")
        la1=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set("")
        en1 = Entry(fenster, width=8, textvariable=self.name)
        self.name.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Vorname")
        la2=Label(self.fenster,textvariable=self.la2_text, width=20, bg="yellow", justify=CENTER)
        self.la2.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set("")
        en2 = Entry(fenster, width=8, textvariable=self.vorname)
        self.en2.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Geburtsdatum")
        la3=Label(self.fenster,textvariable=self.la3_text, width=20, bg="yellow", justify=CENTER)
        self.la3.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set("")
        en3 = Entry(fenster, width=8, textvariable=self.geburtsdatum)
        self.en3.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text=StringVar()
        self.la4_text.set("Geschlecht")
        la4=Label(self.fenster,textvariable=self.la4_text, width=20, bg="yellow", justify=CENTER)
        self.la4.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_1=Button(self.fenster,text="Männlich", width=20, command=self.mann)
        self.bu1_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_2=Button(self.fenster,text="Weiblich", width=20, command=self.frau)
        self.bu1_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text=StringVar()
        self.la5_text.set("Groesse")
        la5=Label(self.fenster,textvariable=self.la5_text, width=20, bg="yellow", justify=CENTER)
        self.la5.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.groesse = StringVar()
        self.groesse.set("")
        en5 = Entry(fenster, width=8, textvariable=self.groesse)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la6_text=StringVar()
        self.la6_text.set("Figur")
        la6=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_1=Button(self.fenster,text="Sportlich", width=20, command=self.sportlich)
        self.bu2_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_2=Button(self.fenster,text="Schlank", width=20, command=self.schlank)
        self.bu2_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_3=Button(self.fenster,text="Vollschlank", width=20, command=self.vollschlank)
        self.bu2_3.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_4=Button(self.fenster,text="Dick", width=20, command=self.dick)
        self.bu2_4.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la7_text=StringVar()
        self.la7_text.set("Rauchverhalten")
        la7=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la7.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_1=Button(self.fenster,text="Raucher", width=20, command=self.raucher)
        self.bu3_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_2=Button(self.fenster,text="Nichtraucher", width=20, command=self.nichtraucher)
        self.bu3_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la8_text=StringVar()
        self.la8_text.set("Sexuelle Orientierung")
        la8=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la8.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_1=Button(self.fenster,text="Heterosexuell", width=20, command=self.heterosexuell)
        self.bu4_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_2=Button(self.fenster,text="Homosexuell", width=20, command=self.homosexuell)
        self.bu4_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_3=Button(self.fenster,text="Bisexuell", width=20, command=self.bisexuell)
        self.bu4_3.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la9_text=StringVar()
        self.la9_text.set("Hobbys")
        la9=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la9.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.hobby = StringVar()
        self.hobby.set("")
        en9 = Entry(fenster, width=8, textvariable=self.hobby)
        self.en9.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la10_text=StringVar()
        self.la10_text.set("Adresse")
        la10=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la10.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.adresse = StringVar()
        self.adresse.set("")
        en10 = Entry(fenster, width=8, textvariable=self.adresse)
        self.en10.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la11_text=StringVar()
        self.la11_text.set("Telefonnummer")
        la11=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la11.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.telefonnummer = StringVar()
        self.telefonnummer.set("")
        en11 = Entry(fenster, width=8, textvariable=self.telefonnummer)
        self.en11.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text=StringVar()
        self.la12_text.set("Email")
        la12=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la12.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.email = StringVar()
        self.email.set("")
        en12 = Entry(fenster, width=8, textvariable=self.email)
        self.en12.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text=StringVar()
        self.la13_text.set("Art d. Benachichtigung über pot. Partner")
        la13=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la13.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_1=Button(self.fenster,text="Telefon", width=20, command=self.telefon)
        self.bu5_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_2=Button(self.fenster,text="Email", width=20, command=self.email)
        self.bu5_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_3=Button(self.fenster,text="Post", width=20, command=self.post)
        self.bu5_3.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text=StringVar()
        self.la14_text.set("Zahlungsart")
        la14=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la14.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu6_1=Button(self.fenster,text="Lastschrift", width=20, command=self.lastschrift)
        self.bu6_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6_2=Button(self.fenster,text="Überweisung", width=20, command=self.ueberweisung)
        self.bu6_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)


        self.la15_text=StringVar()
        self.la15_text.set("IBAN")
        la15=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la15.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.iban = StringVar()
        self.iban.set("")
        en15 = Entry(fenster, width=8, textvariable=self.iban)
        self.en15.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text=StringVar()
        self.la16_text.set("Kontaktaufnahme")
        la16=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la16.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu7_1=Button(self.fenster,text="Telefon", width=20, command=self.aufnahmeTelefon)
        self.bu7_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_2=Button(self.fenster,text="Email", width=20, command=self.aufnahmeEmail)
        self.bu7_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_3=Button(self.fenster,text="Post", width=20, command=self.aufnahmePost)
        self.bu7_3.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_4=Button(self.fenster,text="Chiffre", width=20, command=self.aufnahmeChiffre)
        self.bu7_4.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)


        self.la17_text=StringVar()
        self.la17_text.set("Wunsch-Geschlecht")
        la17=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la17.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu8_1=Button(self.fenster,text="Männlich", width=20, command=self.wunschmann)
        self.bu8_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu9_2=Button(self.fenster,text="Weiblich", width=20, command=self.wunschfrau)
        self.bu9_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text=StringVar()
        self.la18_text.set("Wunsch-Alter")
        la18=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la18.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.walter = StringVar()
        self.walter.set("")
        en18 = Entry(fenster, width=8, textvariable=self.walter)
        self.en18.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text=StringVar()
        self.la19_text.set("Wunsch-Groesse")
        la19=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la19.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.wgroesse = StringVar()
        self.wgroesse.set("")
        en19 = Entry(fenster, width=8, textvariable=self.wgroesse)
        self.en19.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text=StringVar()
        self.la20_text.set("Wunsch-Figur")
        la20=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la20.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_1=Button(self.fenster,text="Sportlich", width=20, command=self.wunschsportlich)
        self.bu10_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_2=Button(self.fenster,text="Schlank", width=20, command=self.wunschschlank)
        self.bu10_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_3=Button(self.fenster,text="Vollschlank", width=20, command=self.wunschvollschlank)
        self.bu10_3.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_4=Button(self.fenster,text="Dick", width=20, command=self.wunschdick)
        self.bu10_4.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la21_text=StringVar()
        self.la21_text.set("Wunsch-Rauchverhalten")
        la21=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la21.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_1=Button(self.fenster,text="Raucher", width=20, command=self.wunschraucher)
        self.bu11_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_2=Button(self.fenster,text="Nichtraucher", width=20, command=self.wunschnichtraucher)
        self.bu11_2.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la22_text=StringVar()
        self.la22_text.set("Wunsch-Hobby")
        la22=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la22.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.whobby = StringVar()
        self.whobby.set("")
        en22 = Entry(fenster, width=8, textvariable=self.whobby)
        self.en22.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu1_1=Button(self.fenster,text="Signalgeber Einfach", width=20, command=self.mann)
        self.bu1_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)


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

        def Telefon(self):
            self.kontaktaufnahme = "telefon"

        def Email(self):
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
