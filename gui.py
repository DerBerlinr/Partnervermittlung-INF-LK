from tkinter import *
from bewerber import *
from haupt import *
from abstrakterFinder import *
from finder1 import *
from finder2 import *
from finder3 import *
import sqlite3
from gui_ausgabe import *




class GUI(Tk,Bewerber):
    def __init__(self):
        Tk.__init__(self)
        self.haupt = Haupt()
        self.finder1 = Finder1()
        Bewerber.__init__(self)

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#696969"

        abstand_x=3
        abstand_y=3

        groesse = 20

        self.la1_text=StringVar()
        self.la1_text.set("Name")
        self.la1=Label(rahmen1,textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set("")
        self.en1 = Entry(rahmen1, width=groesse, textvariable=self.name)
        self.en1.grid(row=1,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Vorname")
        self.la2=Label(rahmen1,textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=2,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set("")
        self.en2 = Entry(rahmen1, width=groesse, textvariable=self.vorname)
        self.en2.grid(row=2,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("abc")
        self.la3=Label(rahmen1,textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=3,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.abc = StringVar()
        self.abc.set("")
        self.en3 = Entry(rahmen1, width=groesse, textvariable=self.abc)
        self.en3.grid(row=3,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text=StringVar()
        self.la4_text.set("Geschlecht")
        self.la4=Label(rahmen1,textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=4,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_1=Button(rahmen1,text="Maennlich", width=groesse, command=self.mann)
        self.bu1_1.grid(row=4,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1_2=Button(rahmen1,text="Weiblich", width=groesse, command=self.frau)
        self.bu1_2.grid(row=4,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text=StringVar()
        self.la5_text.set("Groesse")
        self.la5=Label(rahmen1,textvariable=self.la5_text, width=groesse, bg=farbe, justify=CENTER)
        self.la5.grid(row=5,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.groesse = StringVar()
        self.groesse.set("")
        self.en5 = Entry(rahmen1, width=groesse, textvariable=self.groesse)
        self.en5.grid(row=5,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la6_text=StringVar()
        self.la6_text.set("Figur")
        self.la6=Label(rahmen1,textvariable=self.la6_text, width=groesse, bg=farbe, justify=CENTER)
        self.la6.grid(row=6,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_1=Button(rahmen1,text="Sportlich", width=groesse, command=self.sportlich)
        self.bu2_1.grid(row=6,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_2=Button(rahmen1,text="Schlank", width=groesse, command=self.schlank)
        self.bu2_2.grid(row=6,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_3=Button(rahmen1,text="Vollschlank", width=groesse, command=self.vollschlank)
        self.bu2_3.grid(row=6,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2_4=Button(rahmen1,text="Dick", width=groesse, command=self.dick)
        self.bu2_4.grid(row=6,column=4,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la7_text=StringVar()
        self.la7_text.set("Rauchverhalten")
        self.la7=Label(rahmen1,textvariable=self.la7_text, width=groesse, bg=farbe, justify=CENTER)
        self.la7.grid(row=7,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_1=Button(rahmen1,text="Raucher", width=groesse, command=self.raucher)
        self.bu3_1.grid(row=7,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3_2=Button(rahmen1,text="Nichtraucher", width=groesse, command=self.nichtraucher)
        self.bu3_2.grid(row=7,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la8_text=StringVar()
        self.la8_text.set("Sexuelle Orientierung")
        self.la8=Label(rahmen1,textvariable=self.la8_text, width=groesse, bg=farbe, justify=CENTER)
        self.la8.grid(row=8,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_1=Button(rahmen1,text="Heterosexuell", width=groesse, command=self.heterosexuell)
        self.bu4_1.grid(row=8,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_2=Button(rahmen1,text="Homosexuell", width=groesse, command=self.homosexuell)
        self.bu4_2.grid(row=8,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu4_3=Button(rahmen1,text="Bisexuell", width=groesse, command=self.bisexuell)
        self.bu4_3.grid(row=8,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la9_text=StringVar()
        self.la9_text.set("Hobbys")
        self.la9=Label(rahmen1,textvariable=self.la9_text, width=groesse, bg=farbe, justify=CENTER)
        self.la9.grid(row=9,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.hobby = StringVar()
        self.hobby.set("")
        self.en9 = Entry(rahmen1, width=groesse, textvariable=self.hobby)
        self.en9.grid(row=9,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la10_text=StringVar()
        self.la10_text.set("Adresse")
        self.la10=Label(rahmen1,textvariable=self.la10_text, width=groesse, bg=farbe, justify=CENTER)
        self.la10.grid(row=10,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.adresse = StringVar()
        self.adresse.set("")
        self.en10 = Entry(rahmen1, width=groesse, textvariable=self.adresse)
        self.en10.grid(row=10,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la11_text=StringVar()
        self.la11_text.set("Telefonnummer")
        self.la11=Label(rahmen1,textvariable=self.la11_text, width=groesse, bg=farbe, justify=CENTER)
        self.la11.grid(row=11,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.telefonnummer = StringVar()
        self.telefonnummer.set("")
        self.en11 = Entry(rahmen1, width=groesse, textvariable=self.telefonnummer)
        self.en11.grid(row=11,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la12_text=StringVar()
        self.la12_text.set("Email")
        self.la12=Label(rahmen1,textvariable=self.la12_text, width=groesse, bg=farbe, justify=CENTER)
        self.la12.grid(row=12,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.email = StringVar()
        self.email.set("")
        self.en12 = Entry(rahmen1, width=groesse, textvariable=self.email)
        self.en12.grid(row=12,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la13_text=StringVar()
        self.la13_text.set("Art d. Benachrichtigung ueber pot. Partner")
        self.la13=Label(rahmen1,textvariable=self.la13_text, width=groesse, bg=farbe, justify=CENTER)
        self.la13.grid(row=13,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_1=Button(rahmen1,text="Telefon", width=groesse, command=self.telefon)
        self.bu5_1.grid(row=13,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_2=Button(rahmen1,text="Email", width=groesse, command=self.email)
        self.bu5_2.grid(row=13,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu5_3=Button(rahmen1,text="Post", width=groesse, command=self.post)
        self.bu5_3.grid(row=13,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la14_text=StringVar()
        self.la14_text.set("Zahlungsart")
        self.la14=Label(rahmen1,textvariable=self.la14_text, width=groesse, bg=farbe, justify=CENTER)
        self.la14.grid(row=14,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6_1=Button(rahmen1,text="Lastschrift", width=groesse, command=self.lastschrift)
        self.bu6_1.grid(row=14,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu6_2=Button(rahmen1,text="Ueberweisung", width=groesse, command=self.ueberweisung)
        self.bu6_2.grid(row=14,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la15_text=StringVar()
        self.la15_text.set("IBAN")
        self.la15=Label(rahmen1,textvariable=self.la15_text, width=groesse, bg=farbe, justify=CENTER)
        self.la15.grid(row=15,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.iban = StringVar()
        self.iban.set("")
        self.en15 = Entry(rahmen1, width=groesse, textvariable=self.iban)
        self.en15.grid(row=15,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la16_text=StringVar()
        self.la16_text.set("Kontaktaufnahme")
        self.la16=Label(rahmen1,textvariable=self.la16_text, width=groesse, bg=farbe, justify=CENTER)
        self.la16.grid(row=16,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_1=Button(rahmen1,text="Telefon", width=groesse, command=self.aufnahmeTelefon)
        self.bu7_1.grid(row=16,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_2=Button(rahmen1,text="Email", width=groesse, command=self.aufnahmeEmail)
        self.bu7_2.grid(row=16,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_3=Button(rahmen1,text="Post", width=groesse, command=self.aufnahmePost)
        self.bu7_3.grid(row=16,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu7_4=Button(rahmen1,text="Chiffre", width=groesse, command=self.aufnahmeChiffre)
        self.bu7_4.grid(row=16,column=4,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la17_text=StringVar()
        self.la17_text.set("Wunsch-Geschlecht")
        self.la17=Label(rahmen1,textvariable=self.la17_text, width=groesse, bg=farbe, justify=CENTER)
        self.la17.grid(row=17,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu8_1=Button(rahmen1,text="Maennlich", width=groesse, command=self.wunschmann)
        self.bu8_1.grid(row=17,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu9_2=Button(rahmen1,text="Weiblich", width=groesse, command=self.wunschfrau)
        self.bu9_2.grid(row=17,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la18_text=StringVar()
        self.la18_text.set("Wunsch.abc")
        self.la18=Label(rahmen1,textvariable=self.la18_text, width=groesse, bg=farbe, justify=CENTER)
        self.la18.grid(row=18,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.walter = StringVar()
        self.walter.set("")
        self.en18 = Entry(rahmen1, width=groesse, textvariable=self.walter)
        self.en18.grid(row=18,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la19_text=StringVar()
        self.la19_text.set("Wunsch-Groesse")
        self.la19=Label(rahmen1,textvariable=self.la19_text, width=groesse, bg=farbe, justify=CENTER)
        self.la19.grid(row=19,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.wgroesse = StringVar()
        self.wgroesse.set("")
        self.en19 = Entry(rahmen1, width=groesse, textvariable=self.wgroesse)
        self.en19.grid(row=19,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la20_text=StringVar()
        self.la20_text.set("Wunsch-Figur")
        self.la20=Label(rahmen1,textvariable=self.la20_text, width=groesse, bg=farbe, justify=CENTER)
        self.la20.grid(row=20,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_1=Button(rahmen1,text="Sportlich", width=groesse, command=self.wunschsportlich)
        self.bu10_1.grid(row=20,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_2=Button(rahmen1,text="Schlank", width=groesse, command=self.wunschschlank)
        self.bu10_2.grid(row=20,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_3=Button(rahmen1,text="Vollschlank", width=groesse, command=self.wunschvollschlank)
        self.bu10_3.grid(row=20,column=3,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu10_4=Button(rahmen1,text="Dick", width=groesse, command=self.wunschdick)
        self.bu10_4.grid(row=20,column=4,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la21_text=StringVar()
        self.la21_text.set("Wunsch-Rauchverhalten")
        self.la21=Label(rahmen1,textvariable=self.la21_text, width=groesse, bg=farbe, justify=CENTER)
        self.la21.grid(row=21,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_1=Button(rahmen1,text="Raucher", width=groesse, command=self.wunschraucher)
        self.bu11_1.grid(row=21,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_2=Button(rahmen1,text="Nichtraucher", width=groesse, command=self.wunschnichtraucher)
        self.bu11_2.grid(row=21,column=2,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la22_text=StringVar()
        self.la22_text.set("Wunsch-Hobby")
        self.la22=Label(rahmen1,textvariable=self.la22_text, width=groesse, bg=farbe, justify=CENTER)
        self.la22.grid(row=22,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.whobby = StringVar()
        self.whobby.set("")
        self.en22 = Entry(rahmen1, width=groesse, textvariable=self.whobby)
        self.en22.grid(row=22,column=1,sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu11_2=Button(rahmen1,text="Fertig", width=groesse, command=self.abschicken)
        self.bu11_2.grid(row=23,column=5,sticky=E, padx=abstand_x, pady=abstand_y)

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
        self.benachrichtigung = "telefon"

    def email(self):
        self.benachrichtigung = "email"

    def post(self):
        self.benachrichtigung = "post"

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

    def abschicken(self):

        if self.name == "" or self.vorname == "" or self.abc == "" or self.geschlecht == "" or self.groesse == "" or self.figur == "" or self.rauchverhalten == "" or self.orientierung == "" or self.hobby == "" or self.adresse == "" or self.telefonnummer == "" or self.email == "" or self.benachrichtigung == "" or self.zahlungsart == "" or self.iban == "" or self.kontaktaufnahme == "" or self.wgeschlecht == "" or self.walter == "" or self.wgroesse == "" or self.wfigur == "" or self.wrauchverhalten == "" or self.whobby == "":
            self.la25_text.set("Fehlerhafte Eingabe! - Bitte fuelle alle Felder aus!")
            print("1. Instanz")
            return

        conn = sqlite3.connect('test.db')
        c = conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS benutzer (name TEXT, vorname TEXT, abc TEXT, geschlecht TEXT, groesse TEXT, figur TEXT, rauchverhalten TEXT, orientierung TEXT, hobby TEXT,'
                  ' adresse TEXT, telefonnummer TEXT, email TEXT, benachichtigung TEXT, zahlungsart TEXT, iban TEXT, kontaktaufnahme TEXT, wgeschlecht TEXT, walter TEXT, wgroesse TEXT,'
                  ' wfigur TEXT, wrauchverhalten TEXT, whobby TEXT)')

        c.execute('INSERT INTO benutzer (name, vorname, abc, geschlecht, groesse, figur, rauchverhalten, orientierung, hobby, adresse, telefonnummer, email, benachichtigung, zahlungsart,'
                  ' iban, kontaktaufnahme, wgeschlecht, walter, wgroesse, wfigur, wrauchverhalten, whobby) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                  ,(self.name.get(), self.vorname.get(), self.abc.get(), self.geschlecht, self.groesse.get(), self.figur, self.rauchverhalten, self.orientierung, self.hobby.get(), self.adresse.get(),
                    self.telefonnummer.get(), self.email.get(), self.benachrichtigung, self.zahlungsart, self.iban.get(), self.kontaktaufnahme, self.wgeschlecht, self.walter.get(),
                    self.wgroesse.get(), self.wfigur, self.wrauchverhalten, self.whobby.get()))


        conn.commit()

        neuePerson = Bewerber()

        neuePerson.name = self.name
        neuePerson.vorname = self.vorname
        neuePerson.abc = self.abc
        neuePerson.geschlecht = self.geschlecht
        neuePerson.groesse = self.groesse
        neuePerson.figur = self.figur
        neuePerson.rauchverhalten = self.rauchverhalten
        neuePerson.orientierung = self.orientierung
        neuePerson.hobby = self.hobby
        neuePerson.adresse = self.adresse
        neuePerson.telefonnummer = self.telefonnummer
        neuePerson.email = self.email
        neuePerson.benachrichtigung = self.benachrichtigung
        neuePerson.zahlungsart = self.zahlungsart
        neuePerson.iban = self.iban
        neuePerson.kontaktaufnahme = self.kontaktaufnahme

        neuePerson.wgeschlecht = self.wgeschlecht
        neuePerson.walter = self.walter.get()
        neuePerson.wgroesse = self.wgroesse.get()
        neuePerson.wfigur = self.wfigur
        neuePerson.wrauchverhalten = self.wrauchverhalten
        neuePerson.whobby = self.whobby.get()

        self.wunschListe = [neuePerson.wgeschlecht, neuePerson.walter, neuePerson.wgroesse, neuePerson.wfigur, neuePerson.wrauchverhalten, neuePerson.whobby]

        print(self.wunschListe)
        print(self.walter)
        self.haupt.personVonGUI(neuePerson)
        a,b = self.finder1.findePartner(self.wunschListe)
        print(a,b)
        a = allah
        b = 3
        die_3_GUI = gui_ausgabe(a, b)


    def test(self):
        print("Hallo")

    def getdata(self):
        return x, y, z,


if __name__ == '__main__':
    dasFenster = GUI()
    mainloop()
