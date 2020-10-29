from Fenster import *

#Start Programm
master = Tk()
start_Fenster = hauptfenster(master)
width = start_Fenster.master.winfo_reqwidth()
height = start_Fenster.master.winfo_reqheight()
screenWidth = start_Fenster.master.winfo_screenwidth()
screenHeight = start_Fenster.master.winfo_screenheight()
start_Fenster.master.geometry(f"+{screenWidth//3}+{screenHeight//4}")
master.mainloop()
#Update Fenster
#oben Datensätze gesamt:  im LZG: 

