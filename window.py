from tkinter import *
from tkinter import ttk


class MainWindow:
    def __init__(self, root):
        # MAIN FRAME
        self.mainFrame = ttk.Frame(root, width=350, height=600)

        # CREATE WIDGETS
        self.loginLabel = ttk.Label(self.mainFrame, text='LOGIN', font='Roboto 18 bold')

        self.emailVar = StringVar()
        self.emailLabel = ttk.Label(self.mainFrame, text='Email ', font='Helvetica 12')
        self.emailEntry = ttk.Entry(self.mainFrame, textvariable=self.emailVar,
                                    width=25)

        self.passwordVar = StringVar()
        self.passwrodLabel = ttk.Label(self.mainFrame, text='Password ', font='Helvetica 12')
        self.passwordEntry = ttk.Entry(self.mainFrame, textvariable=self.passwordVar,
                                       width=25)

        self.rememberVar = StringVar()
        self.checkRemember = ttk.Checkbutton(self.mainFrame, textvariable=self.rememberVar)
        self.labelRemember = ttk.Label(self.mainFrame, text='Remember me', font='Helvetica 11')

        self.loginButton = ttk.Button(self.mainFrame, text='LOGIN', style='Accent.TButton')
        self.loginButton.configure(width=20)

        self.orLoginLabel = ttk.Label(self.mainFrame, text='Or login with')

        self.facebookButton = ttk.Button(self.mainFrame, text='Facebook')
        self.facebookButton.configure(width=15)
        self.googleButton = ttk.Button(self.mainFrame, text='Google')
        self.googleButton.configure(width=15)

        self.signLabel = ttk.Label(self.mainFrame, text='Not a member?', font='Helvetica 11')
        self.signUpLabel = ttk.Label(self.mainFrame, text='Sign up now', font='Helvetica 11 underline',
                                     cursor='hand2')

        # FIRST ACTION
        self.draw_widgets()

    def draw_widgets(self):
        # DRAW MAIN FRAME
        self.mainFrame.grid(row=0, column=0, sticky='n', pady=(100, 0))

        # DRAW WIDGETS
        self.loginLabel.grid(row=0, column=0, columnspan=2, padx=(0, 0), pady=(30, 30), sticky='ns')

        self.emailLabel.grid(row=1, column=0, padx=(80, 0), pady=(5, 30), sticky='w')
        self.emailEntry.grid(row=1, column=1, padx=(0, 60), pady=(0, 30))

        self.passwrodLabel.grid(row=2, column=0, padx=(80, 0), pady=(5, 10), sticky='w')
        self.passwordEntry.grid(row=2, column=1, padx=(0, 60), pady=(0, 10))

        self.checkRemember.grid(row=3, column=0, columnspan=2, padx=(0, 60), pady=(0, 0))
        self.labelRemember.grid(row=3, column=1, columnspan=2, padx=(0, 110), pady=(5, 0))

        self.loginButton.grid(row=4, column=0, columnspan=3, padx=(0, 0), pady=(30, 30), sticky='ns')

        self.orLoginLabel.grid(row=5, column=0, columnspan=3, padx=(0, 0), pady=(0, 30), sticky='ns')

        self.facebookButton.grid(row=6, column=0, columnspan=3, padx=(70, 250), pady=(0, 70))
        self.googleButton.grid(row=6, column=1, columnspan=3, padx=(0, 0), pady=(0, 70))

        self.signLabel.grid(row=7, column=0, columnspan=3, padx=(0, 90), pady=(20, 40), sticky='ns')
        self.signUpLabel.grid(row=7, column=1, columnspan=3, padx=(0, 70), pady=(20, 40), sticky='ns')
