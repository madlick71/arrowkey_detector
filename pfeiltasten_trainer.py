import tkinter as tk
import random
import time


class MyCoolApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Pfeiltasten-Trainer')
        self.root.geometry('400x300')
        # Farben
        self.farbe_vorgabe = '#ff9933'
        self.farbe_richtig = 'green'
        self.farbe_falsch = 'red'
        # sich Sachen merken
        self.button_pressed = None
        self.next_button = None
        self.clicks = 0
        self.clicks_correct = 0
        # tk.Buttons
        self.button_left_arrow = tk.Button(self.root, text=u'\u2BC7')
        self.button_left_arrow.place(x=10, y=50, width=100, height=30)
        self.button_right_arrow = tk.Button(self.root, text=u'\u2BC8')
        self.button_right_arrow.place(x=120, y=50, width=100, height=30)
        self.button_up_arrow = tk.Button(self.root, text=u'\u2BC5')
        self.button_up_arrow.place(x=65, y=10, width=100, height=30)
        self.button_down_arrow = tk.Button(self.root, text=u'\u2BC6')
        self.button_down_arrow.place(x=65, y=90, width=100, height=30)
        self.button_close = tk.Button(
            self.root, text='Beenden', command=self.root.quit)
        self.button_close.place(x=270, y=250, width=100, height=30)
        # Textausgabe
        self.label = tk.Label(self.root, text="Los geht's!")
        self.label.config(font=('', 14))
        self.label.place(x=100, y=130, width=200, height=30)
        # Textausgabe Statistik
        self.label_stat_1 = tk.Label(self.root, text='')
        self.label_stat_1.config(font=('', 12))
        self.label_stat_1.place(x=100, y=180, width=200, height=20)
        self.label_stat_2 = tk.Label(self.root, text='')
        self.label_stat_2.config(font=('', 12))
        self.label_stat_2.place(x=100, y=200, width=200, height=20)
        # auf Pfeiltasten hören
        self.root.bind("<Up>", self.up)
        self.root.bind("<Down>", self.down)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)
        # erste Taste farblich markieren
        self.choose_next_button()
        # Fenster starten
        self.root.mainloop()

    def up(self, event):
        self.press_button(self.button_up_arrow)

    def down(self, event):
        self.press_button(self.button_down_arrow)

    def left(self, event):
        self.press_button(self.button_left_arrow)

    def right(self, event):
        self.press_button(self.button_right_arrow)

    def choose_next_button(self):
        all_buttons = [self.button_right_arrow, self.button_left_arrow,
                       self.button_up_arrow, self.button_down_arrow]
        buttons = []
        for button in all_buttons:
            if (button != self.button_pressed):
                buttons.append(button)
        # alle Tasten bis auf den gerade gedrückten grau färben
        for button in buttons:
            button.config(background='#eeeeee')
        # nächste Taste zufällig auswählen und farblich markieren
        self.next_button = random.choice(buttons)
        self.next_button.after(50, lambda:  self.next_button.config(
            background=self.farbe_vorgabe))

    def press_button(self, button):
        self.button_pressed = button
        self.clicks = self.clicks + 1
        # gedrückte Taste simulieren
        self.button_pressed.config(relief=tk.SUNKEN)
        self.button_pressed.after(
            100, lambda:  self.button_pressed.config(relief=tk.RAISED))
        # prüfen, welche Taste gedrückt wurde
        ok = self.check_which_pressed()
        # nächste Taste vorgeben
        if (ok == True):
            self.choose_next_button()

    def check_which_pressed(self):
        if self.button_pressed == self.next_button:
            self.clicks_correct = self.clicks_correct + 1
            wrong = self.clicks - self.clicks_correct
            self.label.configure(text='yeah!  :D')
            self.label_stat_1.configure(
                text='Richtig: ' + str(self.clicks_correct))
            self.label_stat_2.configure(text='Falsch: ' + str(wrong))
            self.button_pressed.config(background=self.farbe_richtig)
            self.button_pressed.after(
                200, lambda:  self.button_pressed.config(background='#eeeeee'))
            return True
        else:
            self.label.configure(text='nope!  :(')
            self.label_stat_1.configure(
                text='Richtig: ' + str(self.clicks_correct))
            wrong = self.clicks - self.clicks_correct
            self.label_stat_2.configure(text='Falsch: ' + str(wrong))
            self.button_pressed.config(background=self.farbe_falsch)
            self.button_pressed.flash()
            self.button_pressed.config(background='#eeeeee')
            return False


app = MyCoolApp()
