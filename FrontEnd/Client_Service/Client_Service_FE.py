import sqlite3
from tkinter import *
from tkinter import ttk


class Client_Service:
    def main(self):
        def DisplayForm():
            # creating window
            Window = Tk()
            # setting width and height for window
            Window.geometry("800x200")
            Window.geometry("1301x728")
            Window.minsize(1301, 728)
            Window.maxsize(1301, 728)
            Window.title("Service Client")
            global tree
            global SEARCH
            SEARCH = StringVar()
            # creating frame
            TopViewForm = Frame(Window, width=600, bd=1, relief=SOLID)
            TopViewForm.pack(side=TOP, fill=X)
            LeftViewForm = Frame(Window, width=600)
            LeftViewForm.pack(side=LEFT, fill=Y)
            MidViewForm = Frame(Window, width=600)
            MidViewForm.pack(side=RIGHT)
            lbl_text = Label(TopViewForm, text="Bienvenue chez interface service client", font=('verdana', 18), width=600,
                             bg="#1C2833", fg="white")
            lbl_text.pack(fill=X)
            lbl_txtsearch = Label(LeftViewForm, text="Search", font=('verdana', 15))
            lbl_txtsearch.pack(side=TOP, anchor=W)

            search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
            search.pack(side=TOP, padx=10, fill=X)
            btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
            btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
            btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
            btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

            # setting scrollbar
            scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
            scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
            tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"),
                                selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                                xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            # setting headings for the columns
            tree.heading('Student Id', text=" Id", anchor=W)
            tree.heading('Name', text="Nom", anchor=W)
            tree.heading('Contact', text="Age", anchor=W)
            tree.heading('Email', text="Genre", anchor=W)
            tree.heading('Rollno', text="Email", anchor=W)
            tree.heading('Branch', text="Role", anchor=W)
            # setting width of the columns
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=100)
            tree.column('#2', stretch=NO, minwidth=0, width=150)
            tree.column('#3', stretch=NO, minwidth=0, width=80)
            tree.column('#4', stretch=NO, minwidth=0, width=120)
            tree.pack()
            DisplayData()

        # function to search data
        def SearchRecord():
            if SEARCH.get() != "":
                tree.delete(*tree.get_children())
                conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
                cursor = conn.execute("SELECT * FROM User WHERE name LIKE ?",
                                      ('%' + str(SEARCH.get()) + '%',))
                fetch = cursor.fetchall()
                # loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                cursor.close()
                conn.close()

        # defining function to access data from SQLite database
        def DisplayData():
            tree.delete(*tree.get_children())
            conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
            cursor = conn.execute("SELECT * FROM User")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()

        DisplayForm()
        mainloop()

    main(self=True)
