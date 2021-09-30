import tkinter as tk
from start_page import StartPage
from singup_page import SingupPage
from success_page import SuccessPage


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

        self.frames = {}
        for f in (StartPage, SingupPage, SuccessPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()


if __name__ == '__main__':
    login_app = LoginApp()
    login_app.mainloop()
