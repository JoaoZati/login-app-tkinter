import tkinter as tk


class SuccessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = '#212529'
        self.bg_frames = '#6c757d'
        self.config(bg=self.bg)

        frame_app = tk.Frame(self, bg=self.bg, height=125)
        frame_app.pack(expand=True, fill='both')
        label_my_app = tk.Label(frame_app, text='My App', bg=self.bg,
                                fg='Yellow', font=('Arial', 24))
        label_my_app.pack(expand=True, fill='both')

        list_frames = [tk.Frame(self, bg=self.bg_frames) for _ in range(2)]
        for indice, frame in enumerate(list_frames):
            frame.pack(expand=True, fill='both')
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)

        self.text_label = 'Login\nSuccessful'
        label_login = tk.Label(list_frames[0], text=self.text_label, bg=self.bg_frames, fg='White',
                               font=('Arial', 30))
        label_login.grid(row=0, column=0)

        self.button_logout = tk.Button(list_frames[1], text='Logout', bg='#495057', highlightthickness=0,
                                       width=20)
        self.button_logout.grid(row=0, column=0)
