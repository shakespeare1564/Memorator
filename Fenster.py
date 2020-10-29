import os
import sys
from tkinter import *
from tkinter import ttk
import datetime
import time
import xlrd
import sqlite3


class hauptfenster():
    def __init__(self, master):
        self.master = master
        self.anzahl_Dateien_Heute = StringVar()
        self.Heute_Text = "Lernkarteien heute " + \
            time.strftime("(%d.%m.%Y):", time.localtime())
        self.master.title("Memorator - Auswahl")
        self.master.geometry("320x200")
        self.master.config(bg="black")
        self.master.bind("<FocusOut>", self.on_focus_out)
        self.master.bind('<Escape>', self.quit)
        self.mainframe = Frame(self.master).place(x=0, y=200)
        # self.Bild_test = PhotoImage(file = "/Users/shakespeare1564/Desktop/sublime/Quellen/tenor.gif", self.master)
        # self.Bild_suchen = PhotoImage(file = "/Users/shakespeare1564/Desktop/sublime/python/Memorator/Programm-Bilder/suchen_background.gif", self.master)
        self.style = ttk.Style()
        self.style.configure(
            "Blue.TButton", foreground="blue", background="blue")
        self.style.configure("Red.TButton", foreground="red",
                             background="red", image='')
        self.style.configure(
            "White.TLabel", foreground="green", highlightbackground="black")
        ttk.Button(self.mainframe, text="heute", command=self.heuteClick).place(
            x=10, y=10, width=80, height=30)
        ttk.Button(self.mainframe, text="2").place(
            x=10, y=50, width=80, height=30)
        ttk.Button(self.mainframe, text="1").place(
            x=10, y=90, width=80, height=30)
        ttk.Button(self.mainframe, text="0").place(
            x=10, y=130, width=80, height=30)
        ttk.Button(self.mainframe, text="suchen", style="Blue.TButton").place(
            x=100, y=10, width=100, height=30)
        ttk.Button(self.mainframe, text=" Protokoll\n Lernen &\n Suchen").place(
            x=100, y=45, width=100, height=60)
        ttk.Button(self.mainframe, style="Red.TButton", text="neu").place(
            x=210, y=10, width=100, height=30)
        ttk.Button(self.mainframe, text=" Protokoll\n neue\n Karten").place(
            x=210, y=45, width=100, height=60)
        ttk.Button(self.mainframe, text="Statistik").place(
            x=100, y=110, width=210, height=50)
        ttk.Label(self.mainframe, style="White.TLabel",
                  textvariable=self.anzahl_Dateien_Heute).place(x=10, y=170)
        # Verbindung zur Datenbank
        if os.path.exists("memorator.db"):
            print("Datenbank existiert")
            self.connection = sqlite3.connect("memorator.db")
            self.cursor = self.connection.cursor()
            # sys.exit(0) #beendet Programm ohne Fehler
        else:
            # Datenbank erstellen
            self.connection = sqlite3.connect("memorator.db")
            self.cursor = self.connection.cursor()
            # Tabelen erstellen
            self.cursor.execute("CREATE TABLE Begriffe \
                (Nr INTEGER PRIMARY KEY, Datum TEXT NULL, EchtDatum DATE NOT NULL,\
                 Fach TEXT NULL,Thema TEXT NULL, Begriff TEXT NULL, Spezifizierung TEXT NULL,\
                 GrafikA Text NULL, Assoziation INTEGER NULL, Assoziationswert TEXT NULL, Fortsetzung TEXT NULL,\
                 Fortschritt INTEGER NULL, Dateityp TEXT NULL, Switch INTEGER NULL, WDatum DATE NULL,\
                 LearnDateHeute DATE NULL, Memo TEXT NULL, wait DATE NOT NULL, waitCounter INTEGER NOT NULL,\
                 pool DATE NOT NULL)")
            self.connection.commit()
            # Excel-Datei einlesen
            # excel_einlesen()
        # self.aktualisieren()

    def aktualisieren(self):
        self.cursor.execute("SELECT COUNT(*) FROM Begriffe WHERE (EchtDatum = '" + time.strftime('%Y-%m-%d') +
                            "' OR Datum = '0' OR Datum = '1' OR Datum = '2') AND Switch = 1")
        self.rows = self.cursor.fetchall()
        self.anzahl_Dateien_Heute.set(
            self.Heute_Text + " " + str(self.rows[0][0]))
        self.connection.close()
    # Button Actions

    def heuteClick(self):
        # wichtig als Singleton
        t = Toplevel(self.mainframe)
        t.wm_title("Window")
        l = Label(t, text="This is window")
        l.pack(side="right", fill="both", expand=True, padx=100, pady=100)
        width = t.winfo_reqwidth()
        height = t.winfo_reqheight()
        screenWidth = t.winfo_screenwidth()
        screenHeight = t.winfo_screenheight()
        t.geometry(f"+{screenWidth//3}+{screenHeight//4}")
    # Events

    def quit(self, event):
        self.master.withdraw()

    def on_focus_out(self, event):
        print(event.widget, "Fokus raus")
    # Layout-Korrekturen

    def layout_resize(self):
        for child in self.master.winfo_children():
            pass
            # print(child.place(x=x+10))
            # child.place_info()['y'])


# Hilfsfunktionen
def excel_einlesen():
    book = xlrd.open_workbook("Tabelle1.xls",
                              encoding_override="utf-8")
    sheet = book.sheet_by_index(0)
    for i in range(sheet.nrows):
        nr = sheet.cell(i, 0).value
        try:
            datum = int(sheet.cell(i, 1).value)
        except ValueError:
            datum = sheet.cell(i, 1).value
        echtdatum = tupel_in_Date(
            xlrd.xldate_as_tuple(sheet.cell(i, 2).value, 0))
        fach = sheet.cell(i, 3).value
        thema = sheet.cell(i, 4).value
        begriff = sheet.cell(i, 5).value
        spezifizierung = sheet.cell(i, 6).value
        grafikA = sheet.cell(i, 7).value
        assoziation = sheet.cell(i, 8).value
        assoziationswert = sheet.cell(i, 9).value
        fortsetzung = sheet.cell(i, 10).value
        fortschritt = sheet.cell(i, 11).value
        dateityp = sheet.cell(i, 12).value
        switch = sheet.cell(i, 13).value
        wdatum = sheet.cell(i, 14).value
        learndateheute = sheet.cell(i, 15).value
        memo = sheet.cell(i, 16).value
        wait = sheet.cell(i, 17).value
        waitcounter = sheet.cell(i, 18).value
        pool = sheet.cell(i, 19).value
        cursor.execute(f"INSERT INTO Begriffe VALUES ({nr}, '{datum}', '{echtdatum}','{fach}',\
            '{thema}', '{begriff}', '{spezifizierung}', '{grafikA}', {assoziation},\
            '{assoziationswert}', '{fortsetzung}', {fortschritt}, '{dateityp}',\
             {switch}, '{wdatum}', '{learndateheute}', '{memo}', '{wait}',\
             {waitcounter}, '{pool}')")
        connection.commit()


def tupel_in_Date(datum):  # Datum muss im Format YYYY-mm-dd sein (z. B. 2019-08-07)
    datum_monat = ""
    datum_tag = ""
    if datum[1] < 10:
        datum_monat = "0" + str(datum[1])
    else:
        datum_monat = str(datum[1])
    if datum[2] < 10:
        datum_tag = "0" + str(datum[2])
    else:
        datum_tag = str(datum[2])
    return str(datum[0]) + "-" + datum_monat + "-" + datum_tag
