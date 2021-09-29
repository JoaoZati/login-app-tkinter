import tkinter as tk
from start_page import StartPage


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('My App - Login')
        self.geometry('300x500')
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_start_page = StartPage(self, self)
        self.frame_start_page.grid(column=0, row=0)


if __name__ == '__main__':
    login_app = LoginApp()
    login_app.mainloop()
