from tkinter import*
import tkinter as tk
import pymysql



class Reg_Form():
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("700x600")
        self.root.resizable( False, False)
        self.root.title("REGISTRATION FORM")
        self.root.configure(background="#458B74")
        
        self.l= Label(self.root, text="REGISTRATION FORM", font=("Arial 20 bold underline"), foreground="black", background="#698B69")
        self.l.pack(pady=10)
        self.label = Label(self.root, text="NAME*", font=('Georgia 20 bold underline'), foreground="black", background="#698B69")
        self.label.place(x=10 , y=100)
        self.label = Label(self.root, text="PLACE*", font=('Georgia 20 bold underline'), foreground="black", background="#698B69")
        self.label.place(x=10 , y=200)
        self.label = Label(self.root, text="PHONE NUMBER*", font=('Georgia 20 bold underline'), foreground="black", background="#698B69")
        self.label.place(x=10 , y=300)

        self.label = Label(self.root, text="STUDENT ID", font=('Georgia 20 bold underline'), foreground="black", background="#698B69")
        self.label.place(x=10 , y=400)


        self.entry0 = Entry(self.root,font=5,borderwidth=4)
        self.entry0.place(x=300,y=95, width=350, height=45)
        self.entry1 = Entry(self.root,font=5,borderwidth=4)
        self.entry1.place(x=300,y=195, width=350, height=45,)
        self.entry2 = Entry(self.root,font=5,borderwidth=4)
        self.entry2.place(x=300,y=295, width=350, height=45,)
        self.entry3 = Entry(self.root,font=5,borderwidth=4)
        self.entry3.place(x=300,y=395, width=350, height=45,)

        button = Button(self.root, text="SUBMIT", font=('Comic Sans',25), foreground="#F0FFFF", background="#8B8378", command= self.submit)
        button.place(x=10, y=500)
        button = Button(self.root, text="UPDATE", font=('Comic Sans',25), foreground="#F0FFFF", background="#8B8378", command= self.update)
        button.place(x=190, y=500)
        button = Button(self.root, text="VIEW", font=('Comic Sans',25), foreground="#F0FFFF", background="#8B8378", command= self.view)
        button.place(x=380, y=500)
        button = Button(self.root, text="DELETE", font=('Comic Sans',25), foreground="#F0FFFF", background="#8B8378", command= self.display)
        button.place(x=530, y=500)

        self.root.mainloop()
        
    def submit(self):
        print(self.entry0.get())
        print(self.entry1.get())
        print(self.entry2.get())
        print(self.entry3.get())


        try:
            db= pymysql.connect(host='localhost', user='root', password='', database='registration_form', port=3306)
            cu= db.cursor()
            cu.execute("INSERT INTO `reg_form`( `s_Name`, `s_Place`, `s_Phone_Number`) VALUES (%s,%s,%s)", (self.entry0.get(), self.entry1.get(), self.entry2.get()))
            db.commit()
        except:
            print('SQLError')

        self.entry0.delete(0,'end')
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        


    def update(self):
        print(self.entry0.get())
        print(self.entry1.get())
        print(self.entry2.get())
        print(self.entry3.get())
        
        try:
            db= pymysql.connect(host='localhost', user='root', password='', database='registration_form', port=3306)
            cu= db.cursor()
            cu.execute("UPDATE `reg_form` SET `s_Name`=%s, `s_Place`= %s ,`s_Phone_Number`=%s WHERE `s_id`=%s", (self.entry0.get(),self.entry1.get(), self.entry2.get(), self.entry3.get()))
            db.commit()

        except:
            print('SQLError')
        
        self.entry0.delete(0,'end')
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')


    def view(self):


        try:
            self.root = tk.Tk()

            self.root.geometry("500x600")
            self.root.resizable( False, False)
            self.root.title("VIEW FORM")
            self.root.configure(background="#8B8378")

            db= pymysql.connect(host='localhost', user='root', password='', database='registration_form', port=3306)
            cu= db.cursor()
            cu.execute("SELECT * FROM `reg_form`")
            i=0
            for r in cu:
                for j in range(len(r)):
                    self.e= Entry(self.root)
                    self.e.grid(row=i , column=j)
                    self.e.insert(END, r[j])
                i=i+1

            db.close()

        except:
            print('SQLError')
    
    
    def display(self):
        print(self.entry0.get())
        print(self.entry1.get())
        print(self.entry2.get())
        print(self.entry3.get())

        try:
            db= pymysql.connect(host='localhost', user='root', password='', database='registration_form', port=3306)
            cu= db.cursor()
            cu.execute("DELETE FROM `reg_form` WHERE s_id=%s", (self.entry3.get()))
            db.commit()

        except:
            print('SQLError')

        self.entry0.delete(0,'end')
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')


ob=Reg_Form()

