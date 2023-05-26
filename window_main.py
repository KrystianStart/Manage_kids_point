import customtkinter as ctk
import window_alert
import window_files_save



def main():
    window = ctk.CTk()
    window.title("Krokusy")
    window.geometry('1500x980')

    button1 = ctk.CTkButton(window,
                            text="Zarządzaj turnusem",
                            font=("Arial", 30),
                            fg_color='#FF0',
                            text_color='#000',
                            hover_color='#AA0',
                            corner_radius=10,
                            command=lambda: window_alert.check_exist(0))
    button1.pack(side='left', padx=100)

    button2 = ctk.CTkButton(window,
                            text="Podglad teraźniejszego \n turnusu",
                            font=("Arial", 30),
                            fg_color='#FF0',
                            text_color='#000',
                            hover_color='#AA0',
                            corner_radius=10,
                            command=lambda: window_alert.check_exist(1))
    button2.pack(side='left', padx=100)

    button3 = ctk.CTkButton(window,
                            text="Dodaj nowy turnus",
                            font=("Arial", 30),
                            fg_color='#FF0',
                            text_color='#000',
                            hover_color='#AA0',
                            corner_radius=10,
                            command=window_files_save.numerate_files)
    button3.pack(side='left', padx=100)

    window.mainloop()
