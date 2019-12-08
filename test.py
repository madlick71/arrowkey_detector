from msvcrt import getch
from tkinter import Tk, Frame, Label, Entry, Button
""" 
while True:
    keycode = ord(getch())
    #print('keycode', keycode)
    if keycode == 80:
        print('arrow down')
    elif keycode == 72:
        print('arrow up')
    elif keycode == 77:
        print('arrow right')
    elif keycode == 75:
        print('arrow left')
    elif keycode == 27:  # ESC
        break
 """


def Button_Zaehlen_Click():
    stand = int(inputZaehler.get())
    if stand > 0:
        # Zähler aktualisieren
        stand = stand - 1
        inputZaehler.delete(0, 'end')
        inputZaehler.insert(0, str(stand))
        tkFenster.after(1000, Button_Zaehlen_Click)


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Test")
tkFenster.geometry("400x300")
# Rahmen Zähler
frameZaehler = Frame(master=tkFenster,
                     background="#dddddd")
frameZaehler.place(x=50, y=50, width=300, height=220)
# Überschrift für den Zähler
labelTimer = Label(master=frameZaehler,
                   text="Timer",
                   background="#dddddd")
labelTimer.place(x=10, y=10, width=40, height=30)
# Eingabefeld für den Zähler
inputZaehler = Entry(master=frameZaehler,
                     background="white")
inputZaehler.insert(0, "30")
inputZaehler.place(x=10, y=70, width=100, height=20)
# Button zum Herunterzählen
buttonZaehlen = Button(master=frameZaehler,
                       text="Herunterzählen",
                       command=Button_Zaehlen_Click)
buttonZaehlen.place(x=10, y=100, width=100, height=30)

# Aktivierung des Fensters
tkFenster.mainloop()
