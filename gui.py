from Tkinter import *


class GUI:
    def __init__(self):
        self.fenster=Tk()
        self.fenster.geometry("700x700")
        self.fenster.resizable(width="false",height="false")
        self.fenster.title("Partnervermittlung")


        rahmen1=Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()


        self.name = "" E1
        self.vorname = "" E2
        self.geburtsdatum = "" E3
        self.geschlecht = "" B4
        self.groesse = "" E5
        self.figur = "" B6
        self.rauchverhalten = "" B7
        self.orientierung = "" B8
        self.hobby = [] E9
        self.adresse = [] E10
        self.telefonnummer = "" E11
        self.email = "" E12
        self.benachrichtigung = "" B13
        self.zahlungsart = "" B14
        self.iban = "" E15
        self.kontaktaufnahme = "" B16

        self.wgeschlecht = "" B17
        self.walter = "" E18
        self.wgroesse = "" E19
        self.wfigur = "" B20
        self.wrauchverhalten = "" B21
        self.whobby = [] E22


        abstand_x=3
        abstand_y=3

        self.la1=StringVar()
        self.la1=Label(rahmen1,text="Name:")
        self.la1.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.en_name=StringVar()
        en1=Entry(rahmen1,width=20,textvariable=self.en_name)
        en1.grid(row=1,column=1,sticky=W, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la1=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.name = StringVar()
        self.name.set("")
        en1 = Entry(fenster, width=8, textvariable=self.name)
        self.name.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text=StringVar()
        self.la2_text.set("Signalgeber Einfach")
        la2=Label(self.fenster,textvariable=self.la2_text, width=20, bg="yellow", justify=CENTER)
        self.la2_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.vorname = StringVar()
        self.vorname.set("")
        en2 = Entry(fenster, width=8, textvariable=self.vorname)
        self.vorname.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text=StringVar()
        self.la3_text.set("Signalgeber Einfach")
        la3=Label(self.fenster,textvariable=self.la3_text, width=20, bg="yellow", justify=CENTER)
        self.la3_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.geburtsdatum = StringVar()
        self.geburtsdatum.set("")
        en3 = Entry(fenster, width=8, textvariable=self.geburtsdatum)
        self.geburtsdatum.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text=StringVar()
        self.la4_text.set("Signalgeber Einfach")
        la4=Label(self.fenster,textvariable=self.la4_text, width=20, bg="yellow", justify=CENTER)
        self.la4_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la5_text=StringVar()
        self.la5_text.set("Signalgeber Einfach")
        la5=Label(self.fenster,textvariable=self.la5_text, width=20, bg="yellow", justify=CENTER)
        self.la5_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.groesse = StringVar()
        self.groesse.set("")
        en5 = Entry(fenster, width=8, textvariable=self.groesse)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la6_text=StringVar()
        self.la6_text.set("Signalgeber Einfach")
        la6=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la7=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la8=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la9=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.hobby = StringVar()
        self.hobby.set("")
        en9 = Entry(fenster, width=8, textvariable=self.hobby)
        self.hobby.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)                        # muss hier nicht anstatt hobby en9 hin?

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la10=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.adresse = StringVar()
        self.adresse.set("")
        en10 = Entry(fenster, width=8, textvariable=self.adresse)
        self.adresse.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la11=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.telefonnummer = StringVar()
        self.telefonnummer.set("")
        en11 = Entry(fenster, width=8, textvariable=self.telefonnummer)
        self.telefonnummer.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la12=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.email = StringVar()
        self.email.set("")
        en12 = Entry(fenster, width=8, textvariable=self.email)
        self.email.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la13=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la14=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la15=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.iban = StringVar()
        self.iban.set("")
        en15 = Entry(fenster, width=8, textvariable=self.iban)
        self.iban.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la16=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la17=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la18=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.walter = StringVar()
        self.walter.set("")
        en18 = Entry(fenster, width=8, textvariable=self.walter)
        self.walter.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la19=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.wgroesse = StringVar()
        self.wgroesse.set("")
        en19 = Entry(fenster, width=8, textvariable=self.wgroesse)
        self.wgroesse.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la20=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la21=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la22=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.whobby = StringVar()
        self.whobby.set("")
        en22 = Entry(fenster, width=8, textvariable=self.whobby)
        self.whobby.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)

        self.la1_text=StringVar()
        self.la1_text.set("Signalgeber Einfach")
        la23=Label(self.fenster,textvariable=self.la1_text, width=20, bg="yellow", justify=CENTER)
        self.la1_text.grid(row=1,column=0,sticky=E, padx=abstand_x, pady=abstand_y)


        self.bu1_1=Button(self.fenster,text="Signalgeber Einfach", width=20, command=self.mann)
        self.bu1_1.grid(row=1,colomn=1,sticky=E, padx=abstand_x, pady=abstand_y)


        def mann(self):
            self.geschlecht = "m"

    def getdata(self):
        return x, y, z,

if __name__ == '__main__':
    dasFenster = GUI()
    mainloop()
