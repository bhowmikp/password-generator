try:
    import password_generator as generator
    import_correctly = True
except:
    import_correctly = False
    
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, highlightbackground="green", highlightthickness=1)
        self.create_widgets()        
        
    def user_info(self, label_text):
        label = Label(text=label_text, bg='#2A2C2B', fg="white")
        text = Entry()
        return label, text
    
    def password_criteria(self, label_text):
        button = Checkbutton(bg='#2A2C2B', onvalue = 1, offvalue = 0)
        label = Label(text=label_text, bg='#2A2C2B', fg="white")
        return button, label
    
    def create_widgets(self):
        welcome = Label(text='Generates password for account', bg='#2A2C2B', fg="white")
        welcome.grid(row=0, column=1, columnspan=2, padx=125)
        
        account, account_text = self.user_info("Account For: ")
        account.grid(row=1, column=1, sticky = "E")
        account_text.grid(row=1, column=2)
        
        
    
def main():
    root = Tk()
    app = Application(master=root)
    app.master.title("Password Generator")
    root.minsize(500, 500)
    root.maxsize(500, 500)    
    

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)    
    root.config(bg='#2A2C2B', menu=menubar)
    app.mainloop()
    #root.destroy()

if __name__ == "__main__":
    main()