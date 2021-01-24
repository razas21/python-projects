import tkinter as tk
from tkinter import font as tkfont
import tkinter.messagebox
import base64

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (RegisterPage, LoginPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        homeFrame = tk.Frame(self)
        homeFrame.pack()

        label = tk.Label(master=homeFrame, text="Welcome!", font=controller.title_font)
        label.grid(row=0, column=1, padx=15, pady=15)

        button1 = tk.Button(master=homeFrame, text="Login",
                            command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(master=homeFrame, text="Register",
                            command=lambda: controller.show_frame("RegisterPage"))

        button1.grid(row=2, column=1, pady=5)
        button2.grid(row=3, column=1, pady=5)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        titleFrame = tk.Frame(master=self)
        titleFrame.pack()
        entryFrame = tk.Frame(master=self)
        entryFrame.pack()
        buttonFrame = tk.Frame(self)
        buttonFrame.pack(pady=5)

        label = tk.Label(master=titleFrame, text="Login Page", font=controller.title_font)
        userLabel = tk.Label(master=entryFrame, text='Username:')
        passLabel = tk.Label(master=entryFrame, text='Password: ')
        self.userEntry = tk.Entry(master=entryFrame)
        self.passEntry = tk.Entry(master=entryFrame, show="*")

        label.grid(row=0, column=0, padx=5, pady=5)
        self.userEntry.grid(row=0, column=1, padx=10, pady=5)
        userLabel.grid(row=0,column=0,padx=5, pady=5)
        self.passEntry.grid(row=1, column=1, padx=10, pady=5)
        passLabel.grid(row=1,column=0,padx=0,pady=5)
        loginButton = tk.Button(self, text="Login", command= self.login)
        homeButton = tk.Button(self, text='\N{LEFTWARDS BLACK ARROW}',
                               command=lambda: controller.show_frame("HomePage"))
        loginButton.pack(padx=15, ipadx=15, side=tk.RIGHT)
        homeButton.pack(padx=10,pady=5, side=tk.LEFT)

    def decrypt(self, x):
        return(base64.b64decode(x[1:]).decode('latin-1'))

    def organize(self):
        f = open("LoginsDataBase.txt", "r")
        content = f.readlines()
        newContent = []
        self.database = {}  # dictionary with user as key and pass as value
        for info in content:
            info = info.split()
            newContent.append(info)
            self.database = dict(newContent)

    def login(self):
        self.organize()
        user = str(self.userEntry.get())
        password = str(self.passEntry.get())

        if user in self.database:
            if (self.decrypt(self.database[user])) == password:
                tk.messagebox.showinfo("Message", "Success!")
                self.userEntry.delete(0, tk.END)
                self.passEntry.delete(0, tk.END)

            else:
                tk.messagebox.showinfo("Error", "Password incorrect.")
                self.passEntry.delete(0, tk.END)

        else:
            tk.messagebox.showinfo("Error", "User does not exist.")
            self.userEntry.delete(0, tk.END)
            self.passEntry.delete(0, tk.END)

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        titleFrame = tk.Frame(master=self)
        titleFrame.pack()
        entryFrame = tk.Frame(master=self)
        entryFrame.pack()
        buttonFrame = tk.Frame(self)
        buttonFrame.pack(pady=5)

        label = tk.Label(master=titleFrame, text="Register Here", font=controller.title_font)
        userLabel = tk.Label(master=entryFrame, text='Username:')
        passLabel = tk.Label(master=entryFrame, text='Password: ')
        self.userEntry = tk.Entry(master=entryFrame)
        self.passEntry = tk.Entry(master=entryFrame)

        label.grid(row=0, column=0, padx=5, pady=5)
        self.userEntry.grid(row=0, column=1, padx=10, pady=5)
        userLabel.grid(row=0,column=0,padx=5, pady=5)
        self.passEntry.grid(row=1, column=1, padx=10, pady=5)
        passLabel.grid(row=1,column=0,padx=0,pady=5)
        RegisterButton = tk.Button(self, text="Register", command = self.createAccount)
        homeButton = tk.Button(self, text='\N{LEFTWARDS BLACK ARROW}',
                               command=lambda: controller.show_frame("HomePage"))
        RegisterButton.pack(padx=15, ipadx=15, side=tk.RIGHT)
        homeButton.pack(padx=10,pady=5, side=tk.LEFT)

    def encrypt(self,x):
        return(base64.b64encode(x.encode('latin-1')))

    def organize(self):
        try:
            f = open("LoginsDataBase.txt", "r")
        except:
            f = open("LoginsDataBase.txt","w")


        content = f.readlines()
        newContent = []
        self.database = {}  # dictionary with user as key and pass as value
        for info in content:
            info = info.split()
            newContent.append(info)
            self.database = dict(newContent)


    def createAccount(self):
        self.organize()
        user = str(self.userEntry.get())
        password = str(self.passEntry.get())

        if user in self.database:
            tk.messagebox.showinfo("Error", "User in use. Try again!")

        elif len(user) == 0:
            tk.messagebox.showinfo("Error", "Enter a valid username!")
        elif len(password) < 5:
            tk.messagebox.showinfo("Error!", "Password must be at least five characters!")

        else:
            info = (user, str(self.encrypt(password)))
            f = open("LoginsDataBase.txt", "a")
            f.write((info[0] + ' ' + info[1]) + '\n')
            tk.messagebox.showinfo("Success!", "Account successfully created!")
            self.userEntry.delete(0, tk.END)
            self.passEntry.delete(0, tk.END)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
