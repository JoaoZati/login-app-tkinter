import tkinter as tk
from backend import Database
from success_page import SuccessPage
from singup_page import SingupPage

database = Database('users.db')


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = '#212529'
        self.bg_frames = '#6c757d'
        self.config(bg=self.bg)

        self.controller = controller

        frame_app = tk.Frame(self, bg=self.bg, height=125)
        frame_app.pack(expand=True, fill='both')
        label_my_app = tk.Label(frame_app, text='My App', bg=self.bg,
                                fg='Yellow', font=('Arial', 24))
        label_my_app.pack(expand=True, fill='both')

        list_frames = [tk.Frame(self, bg=self.bg_frames) for _ in range(5)]

        for indice, frame in enumerate(list_frames):
            frame.pack(expand=True, fill='both')
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)
            if indice < 2:
                frame.grid_columnconfigure(1, weight=2)

        label_username = tk.Label(list_frames[0], text='Username:', bg=self.bg_frames,
                                  font=('Arial', 11))
        label_username.grid(row=0, column=0, sticky='e')

        self.text_username = tk.StringVar()
        self.entry_username = tk.Entry(list_frames[0], textvariable=self.text_username,
                                       width=20, justify='center')
        self.entry_username.grid(row=0, column=1)

        label_password = tk.Label(list_frames[1], text='Password:', bg=self.bg_frames,
                                  font=('Arial', 11))
        label_password.grid(row=0, column=0, sticky='e')

        self.text_password = tk.StringVar()
        self.entry_password = tk.Entry(list_frames[1], textvariable=self.text_password,
                                       width=20, justify='center')
        self.entry_password.grid(row=0, column=1)

        self.text_menssage = ''
        self.label_menssage = tk.Label(list_frames[2], text=self.text_menssage, bg=self.bg_frames, fg='Yellow',
                                       font=('Arial', 15))
        self.label_menssage.grid(row=0, column=0)

        self.button_login = tk.Button(list_frames[3], text='Login', bg='#495057', highlightthickness=0,
                                      width=20, command=self.login_button)
        self.button_login.grid(row=0, column=0)

        self.button_singup = tk.Button(list_frames[4], text='Sing up', bg='#495057', highlightthickness=0,
                                       width=20, command=self.singup)
        self.button_singup.grid(row=0, column=0)

    def login_button(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        bool_login = database.search_data(username, password)
        if bool_login:
            self.controller.show_frame(SuccessPage)
            return

        self.label_menssage.config(text='Wrong username or login\nPlease try again or singup')

    def singup(self):
        self.controller.show_frame(SingupPage)
