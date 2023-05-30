import customtkinter as ctk
import window_alert
import window_files_save
import os


class Main:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Krokusy")
        self.window.geometry('1500x980')
        self.number = 'number'

    def window(self):
        button1 = ctk.CTkButton(self.window,
                                text="Zarządzaj turnusem",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=lambda:  Main.check_exist(self, 1))
        button1.pack(side='left', padx=100)

        button2 = ctk.CTkButton(self.window,
                                text="Podglad teraźniejszego \n turnusu",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=lambda: Main.check_exist(self, 2))
        button2.pack(side='left', padx=100)

        button3 = ctk.CTkButton(self.window,
                                text="Dodaj nowy turnus",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=window_files_save.numerate_files)
        button3.pack(side='left', padx=100)

        self.window.mainloop()
        return self.number

    def check_exist(self, number):
        folder = os.listdir("files")
        if len(folder) == 0:
            return window_alert.window_alert("Nie istnieje jeszcze zaden turnus")
        else:
            self.window.destroy()
            self.number = number

