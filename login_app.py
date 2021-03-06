import tkinter as tk
from start_page import StartPage
from singup_page import SingupPage
from success_page import SuccessPage
from backend import Database

database = Database('users.db')


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

        self.frames[SuccessPage].button_logout.config(command=self.logout)
        self.frames[SingupPage].button_singup.config(command=self.singup)
        self.frames[SingupPage].button_back.config(command=self.back_to_login)

    def show_frame(self, frame):
        frame = self.frames[frame]
        frame.tkraise()

    def logout(self):
        self.frames[StartPage].entry_password.delete(0, tk.END)
        self.frames[StartPage].entry_username.delete(0, tk.END)
        self.frames[StartPage].label_menssage.config(text='')
        self.show_frame(StartPage)

    def singup(self):
        username = self.frames[SingupPage].entry_username.get()
        password = self.frames[SingupPage].entry_password.get()
        confirm_password = self.frames[SingupPage].entry_confirm_password.get()

        dict_verify = {
            username: 'Username field is empty',
            password: 'Password field is empty',
            confirm_password: 'Confirm Password field\nis empty',
            }

        for key, value in dict_verify.items():
            if key == '':
                self.frames[SingupPage].label_menssage.config(text=value)
                return

        if password != confirm_password:
            self.frames[SingupPage].label_menssage.config(text='Passwords not the same')
            return

        try:
            database.insert_data(username, password)
        except:
            self.frames[SingupPage].label_menssage.config(text='Username already exists')
            return

        self.frames[SingupPage].entry_username.delete(0, tk.END)
        self.frames[SingupPage].entry_password.delete(0, tk.END)
        self.frames[SingupPage].entry_confirm_password.delete(0, tk.END)
        self.frames[SingupPage].label_menssage.config(text='')

        self.frames[StartPage].label_menssage.config(text='User successful\nCadastred')
        self.show_frame(StartPage)

    def back_to_login(self):
        self.frames[SingupPage].entry_username.delete(0, tk.END)
        self.frames[SingupPage].entry_password.delete(0, tk.END)
        self.frames[SingupPage].entry_confirm_password.delete(0, tk.END)
        self.frames[SingupPage].label_menssage.config(text='')
        self.frames[StartPage].label_menssage.config(text='')
        self.show_frame(StartPage)


if __name__ == '__main__':
    login_app = LoginApp()
    login_app.mainloop()
