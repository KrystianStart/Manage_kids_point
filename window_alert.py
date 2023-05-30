import customtkinter as ctk


def window_alert(text):

    window = ctk.CTk()
    window.geometry('640x70')

    mylabel = ctk.CTkLabel(window,
                           text=text,
                           font=("Arial", 20))
    mylabel.pack()

    button = ctk.CTkButton(window,
                           text='Okey',
                           font=("Arial", 15),
                           fg_color='#FF0',
                           text_color='#000',
                           hover_color='#AA0',
                           corner_radius=10,
                           command=window.destroy)
    button.pack()
    window.mainloop()

