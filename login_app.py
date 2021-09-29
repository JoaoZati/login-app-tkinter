import tkinter as tk
from start_page import StartPage


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('My App - Login')
        self.geometry('300x500')
        self.resizable(0, 0)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame_start_page = StartPage(container, self)
        self.frame_start_page.grid(row=0, column=0, sticky='nsew')

        self.frame_2 = StartPage(container, self)
        self.frame_2.config(bg='#212529')
        self.frame_2.grid(row=0, column=0, sticky='nsew')

        self.frame_2.tkraise()
        self.frame_start_page.tkraise()


if __name__ == '__main__':
    login_app = LoginApp()
    login_app.mainloop()
