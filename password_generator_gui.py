# password_generator_gui.py

'''Makes gui for password generator'''

try:
    import password_generator as generator
    IMPORT_CORRECTLY = True
except BaseException:
    IMPORT_CORRECTLY = False

from tkinter import Tk, Frame, StringVar, IntVar, Label
from tkinter import Entry, Checkbutton, Button, Menu, TclError


class Application(Frame):
    '''Makes the gui interface'''

    def __init__(self, master):
        '''Calls necessary functions to create the app

        Args:
            master = Tk()
        '''
        self.master = master

        Frame.__init__(self, master, highlightbackground="green",
                       highlightthickness=1)
        self.site = StringVar()
        self.username = StringVar()
        self.length = IntVar()

        self.upper_case_status = IntVar()
        self.lower_case_status = IntVar()
        self.number_status = IntVar()
        self.symbol_status = IntVar()

        self.message = StringVar()
        self.clipboard_message = StringVar()

        self.create_widgets()

    def calculate(self):
        '''Gets all the input from the user and generates password

        Gets all input from the user in the gui and calls the function
        to generate password
        '''
        self.clipboard_message.set("")

        if IMPORT_CORRECTLY is False:
            self.message.set("Code not found")
        elif self.site.get() == "":
            self.message.set("Please enter name of site")
        elif self.username.get() == "":
            self.message.set("Please enter username")
        else:
            try:
                # get all input from gui
                password = generator.generate_password(
                    self.length.get(),
                    self.upper_case_status.get(),
                    self.lower_case_status.get(),
                    self.number_status.get(),
                    self.symbol_status.get())

                self.message.set("Password: " + password)
                if len(password) == self.length.get():
                    self.master.clipboard_clear()
                    self.master.clipboard_append(password)
                    self.clipboard_message.set("Password copied to clipboard")

                    generator.create_file(
                        self.site.get(), self.username.get(), password)

            except TclError:
                self.message.set("Please enter valid length")

    def create_widgets(self):
        '''Creates all the elements inside the frame'''
        row_location = 0

        # welcome message
        Label(
            text='Generates password for account',
            bg='#2A2C2B', fg="white").grid(
                row=row_location, column=1, columnspan=2, padx=125, pady=10)
        row_location += 1

        # get account name
        Label(text="Account For: ", bg='#2A2C2B', fg="white").grid(
            row=row_location, column=1, sticky="E", pady=10)
        Entry(textvariable=self.site).grid(
            sticky="W", row=row_location, column=2)
        row_location += 1

        # get username
        Label(text="Username: ", bg='#2A2C2B', fg="white").grid(
            row=row_location, column=1, sticky="E", pady=10)
        Entry(textvariable=self.username).grid(
            sticky="W", row=row_location, column=2)
        row_location += 1

        # get length
        Label(text="Password Length: ", bg='#2A2C2B', fg="white").grid(
            row=row_location, column=1, sticky="E", pady=10)
        Entry(textvariable=self.length).grid(
            sticky="W", row=row_location, column=2)
        row_location += 1

        # checkboxes
        Checkbutton(bg='#2A2C2B', variable=self.upper_case_status).grid(
            sticky="E", row=row_location, column=1, pady=10)
        Label(text="Uppercase Character [A-Z]", bg='#2A2C2B',
              fg="white").grid(sticky="W", row=row_location, column=2)
        row_location += 1

        Checkbutton(bg='#2A2C2B', variable=self.lower_case_status).grid(
            sticky="E", row=row_location, column=1, pady=10)
        Label(text="Lowercase Character [a-z]", bg='#2A2C2B',
              fg="white").grid(sticky="W", row=row_location, column=2)
        row_location += 1

        Checkbutton(bg='#2A2C2B', variable=self.number_status).grid(
            sticky="E", row=row_location, column=1, pady=10)
        Label(text="Numbers [0-9]", bg='#2A2C2B',
              fg="white").grid(sticky="W", row=row_location, column=2)
        row_location += 1

        Checkbutton(bg='#2A2C2B', variable=self.symbol_status).grid(
            sticky="E", row=row_location, column=1, pady=10)
        Label(text="Symbols [Ex - ?, $]", bg='#2A2C2B',
              fg="white").grid(sticky="W", row=row_location, column=2)
        row_location += 1

        self.upper_case_status.set(True)
        self.lower_case_status.set(True)
        self.number_status.set(True)
        self.symbol_status.set(True)
        self.length.set(30)

        # generate password
        Button(text="Generate Password", command=self.calculate).grid(
            row=row_location, column=1, columnspan=2, pady=20)
        row_location += 1

        # display message
        Label(textvariable=self.message, bg='#2A2C2B', fg="white").grid(
            sticky="W", row=row_location, column=1, padx=125, columnspan=2)
        row_location += 1

        # inform about clipboard
        Label(
            textvariable=self.clipboard_message,
            bg='#2A2C2B',
            fg="white").grid(sticky="W", row=row_location, column=1, padx=125, columnspan=2)


def main():
    '''Makes the application
    '''
    root = Tk()
    app = Application(master=root)
    app.master.title("Password Generator")
    root.minsize(500, 500)
    root.maxsize(600, 600)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(bg='#2A2C2B', menu=menubar)
    app.mainloop()


if __name__ == "__main__":
    main()
