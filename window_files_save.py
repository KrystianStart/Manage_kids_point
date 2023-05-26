import os
from tkinter import filedialog
import shutil
import read_files
import customtkinter as ctk


def create_new():
    folder = os.listdir("files")
    number = len(folder) + 1
    window.destroy()
    load(number)


def numerate_files():
    folder = os.listdir("files")
    if len(folder) == 0:
        load(1)
    else:
        global window

        window = ctk.CTk()
        window.geometry('700x100')
        mylabel = ctk.CTkLabel(window,
                               text="Czy chcesz utworzyc nowy turnus?",
                               font=('Arial', 15),
                               )
        mylabel.pack()
        button1 = ctk.CTkButton(window,
                                text='Tak',
                                font=("Arial", 15),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=create_new)
        button1.pack(side='left', padx=50)

        button2 = ctk.CTkButton(window,
                                text='Nie',
                                font=("Arial", 15),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=window.destroy)
        button2.pack(side='right', padx=50)

        window.mainloop()


def load(number):
    file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=[("Plik Excel", "*.xlsx")])
    if not file_path:
        return
    destination_path = os.path.join("files", f"plik{number}.xlsx")
    shutil.copy(file_path, destination_path)
    read_files.read(number)
