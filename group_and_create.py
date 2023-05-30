import customtkinter as ctk
import main

class Main:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Krokusy")
        self.window.geometry('1500x980')
        self.number = 'number'

    def window(self):
        button1 = ctk.CTkButton(self.window,
                                text="Grupy, pokoje i wychowacy",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=self.window.destroy)
        button1.pack(side='left', padx=50)

        button2 = ctk.CTkButton(self.window,
                                text="Pobierz arkusz excel",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=self.window.destroy)
        button2.pack(side='left', padx=50)

        button3 = ctk.CTkButton(self.window,
                                text="Usun turnus",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=self.window.destroy)
        button3.pack(side='left', padx=50)

        button4 = ctk.CTkButton(self.window,
                                text="Powrot",
                                font=("Arial", 30),
                                fg_color='#FF0',
                                text_color='#000',
                                hover_color='#AA0',
                                corner_radius=10,
                                command=lambda: Main.back(self))
        button4.pack(side='left', padx=50)

        self.window.mainloop()

    def back(self):
        self.window.destroy()
        main.main()
