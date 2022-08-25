import time
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from BackEnd.Services.TechnicienService import *
from BackEnd.Services.IngineerService import *
class Manager:
    def main_Manager():
        dbTech = TechnicienService("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")
        dbIng = IngineerService("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")

        Window = Tk()
        Window.title("Admin Pannel")
        Window.geometry("1431x728")
        Window.minsize(1341, 728)
        Window.maxsize(1341, 728)
        bg = ImageTk.PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/AdminBgPannel.png")
        canvas = Canvas(Window, width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_image(0, 0, image=bg, anchor='nw')



        def resize_image(e):
            global image, resized, image2
            image = Image.open("/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/AdminBgPannel.png")
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')
        Window.bind("<Configure>")

        def Home_Function():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")


        def Tech_Function():
            print("Tech Works")
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")


            name = StringVar()
            age = StringVar()
            gender = StringVar()
            mail = StringVar()
            Role = StringVar()
            password = StringVar()

            frame1 = Frame(Frame1, padx=20, pady=20, bg="#636e72")
            frame1.pack(side=TOP, fill=X)

            lblTitle = Label(frame1, bg="#636e72", text="Gestion", font=("times", 16, "bold"), fg="white", pady=10)
            lblTitle.grid(columnspan=2)

            lblName = Label(frame1, text="Nom ", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblName.grid(row=1, column=0)

            txtName = Entry(frame1, textvariable=name, font=("times", 16), width=43)
            txtName.grid(row=1, column=1)

            lblAge = Label(frame1, text="Age", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblAge.grid(row=2, column=0)

            txtAge = Entry(frame1, font=("times", 16), textvariable=age, width=43)
            txtAge.grid(row=2, column=1)

            lblgen = Label(frame1, text="Genre", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblgen.grid(row=3, column=0)

            cb = ttk.Combobox(frame1, width=41, textvariable=gender, state="readonly", font=("times", 16))
            cb['values'] = ("Male", "Female", "Others")
            cb.grid(row=3, column=1)

            lblAdd = Label(frame1, text="Mail", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblAdd.grid(row=4, column=0)

            txtAdd = Entry(frame1, font=("times", 16), width=43, textvariable=mail)
            txtAdd.grid(row=4, column=1)

            lblCon = Label(frame1, text="Role", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblCon.grid(row=5, column=0)

            txtCon = Entry(frame1, font=("times", 16), textvariable=Role, width=43)
            txtCon.grid(row=5, column=1)
            txtCon.insert(0, "Technicien")
            txtCon.configure(state=DISABLED)


            lblMail = Label(frame1, text="password", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblMail.grid(row=6, column=0)

            txtMail = Entry(frame1, font=("times", 16), textvariable=password, width=43)
            txtMail.grid(row=6, column=1)

            btn_frame = Frame(frame1, bg="#2d3436")
            btn_frame.grid(row=7, column=1, columnspan=4)

            def fetchData():
                table.delete(*table.get_children())
                count = 0
                for row in dbTech.fetch_record():
                    count += 1
                    table.insert("", END, values=(count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

            def addData():
                if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                    messagebox.showinfo("Message", "Please Fill All Records")
                else:
                    dbTech.insert(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get())
                    fetchData()
                    clearData()
                    messagebox.showinfo("Message", "Record Insert Successfully")

            def getrecord(event):
                srow = table.focus()
                data = table.item(srow)
                global row
                row = data['values']
                name.set(row[2])
                age.set(row[3])
                gender.set(row[4])
                Role.set(row[6])
                mail.set(row[7])
                password.set(row[5])

            def updateData():
                if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or cb.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                    messagebox.showinfo("Message", "Please Fill All Records")
                else:
                    dbTech.update_record(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get(),
                                     (row[1]))
                    fetchData()
                    clearData()
                    messagebox.showinfo("Message", "Record Update Successfully")

            def deleteData():
                dbTech.remove_record(row[1])
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Delete Successfully")

            def clearData():
                name.set("")
                age.set("")
                gender.set("")
                Role.set("")
                mail.set("")
                password.set("")

            btnSub = Button(btn_frame, text="Insert", bg="#01a3a4", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=addData)
            btnSub.grid(row=0, column=0)

            btnUp = Button(btn_frame, text="Update", bg="#F79F1F", fg="white", width=6, padx=20, pady=5,
                           font=("times", 16, "bold"), command=updateData)
            btnUp.grid(row=0, column=1)

            btnDel = Button(btn_frame, text="Delete", bg="#ee5253", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=deleteData)
            btnDel.grid(row=0, column=2)

            btnClr = Button(btn_frame, text="Clear", bg="#1289A7", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=clearData)
            btnClr.grid(row=0, column=3)

            myFrame = Frame(Frame1)
            myFrame.place(x=0, y=425, width=1920, height=500)

            style = ttk.Style()
            style.configure("Treeview", font=("times", 15), rowheight=38)
            style.configure("Treeview.Heading", font=("times", 16, "bold"))

            table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7))

            table.column("0", anchor=CENTER,width=70)
            table.column("1", stretch=NO, width=70)
            table.column("3", anchor=CENTER,width=70)
            table.column("6", anchor=CENTER,width=70)

            table.heading("0", text="S.NO")
            table.heading("1", text="ID")
            table.heading("2", text="Nom ")
            table.heading("3", text="AGE")
            table.heading("4", text="Genre")
            table.heading("5", text="Adresse")
            table.heading("6", text="Contact")
            table.heading("7", text="Email")
            table["show"] = 'headings'
            table.bind("<ButtonRelease-1>", getrecord)
            table.pack(fill=X)

            fetchData()

        def Ing_Function():
            print("Ing Works")
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")


            name = StringVar()
            age = StringVar()
            gender = StringVar()
            mail = StringVar()
            Role = StringVar()
            password = StringVar()

            frame1 = Frame(Frame1, padx=20, pady=20, bg="#636e72")
            frame1.pack(side=TOP, fill=X)

            lblTitle = Label(frame1, bg="#636e72", text="Gestion", font=("times", 16, "bold"), fg="white", pady=10)
            lblTitle.grid(columnspan=2)

            lblName = Label(frame1, text="Nom ", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblName.grid(row=1, column=0)

            txtName = Entry(frame1, textvariable=name, font=("times", 16), width=43)
            txtName.grid(row=1, column=1)

            lblAge = Label(frame1, text="Age", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblAge.grid(row=2, column=0)

            txtAge = Entry(frame1, font=("times", 16), textvariable=age, width=43)
            txtAge.grid(row=2, column=1)

            lblgen = Label(frame1, text="Genre", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblgen.grid(row=3, column=0)

            cb = ttk.Combobox(frame1, width=41, textvariable=gender, state="readonly", font=("times", 16))
            cb['values'] = ("Male", "Female", "Others")
            cb.grid(row=3, column=1)

            lblAdd = Label(frame1, text="mail", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblAdd.grid(row=4, column=0)

            txtAdd = Entry(frame1, font=("times", 16), width=43, textvariable=mail)
            txtAdd.grid(row=4, column=1)

            lblCon = Label(frame1, text="Role", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblCon.grid(row=5, column=0)

            txtCon = Entry(frame1, font=("times", 16), textvariable=Role, width=43)
            txtCon.grid(row=5, column=1)
            txtCon.insert(0, "Ingineer")
            txtCon.configure(state=DISABLED)


            lblMail = Label(frame1, text="mot de passe", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
            lblMail.grid(row=6, column=0)

            txtMail = Entry(frame1, font=("times", 16), textvariable=password, width=43)
            txtMail.grid(row=6, column=1)

            btn_frame = Frame(frame1, bg="#2d3436")
            btn_frame.grid(row=7, column=1, columnspan=4)

            def fetchData():
                table.delete(*table.get_children())
                count = 0
                for row in dbIng.fetch_record():
                    count += 1
                    table.insert("", END, values=(count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

            def addData():
                if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                    messagebox.showinfo("Message", "Please Fill All Records")
                else:
                    dbIng.insert(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get())
                    fetchData()
                    clearData()
                    messagebox.showinfo("Message", "Record Insert Successfully")

            def getrecord(event):
                srow = table.focus()
                data = table.item(srow)
                global row
                row = data['values']
                name.set(row[2])
                age.set(row[3])
                gender.set(row[4])
                Role.set(row[6])
                password.set(row[7])
                mail.set(row[5])

            def updateData():
                if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or cb.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                    messagebox.showinfo("Message", "Please Fill All Records")
                else:
                    dbIng.update_record(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get(),
                                     (row[1]))
                    fetchData()
                    clearData()
                    messagebox.showinfo("Message", "Record Update Successfully")

            def deleteData():
                dbIng.remove_record(row[1])
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Delete Successfully")

            def clearData():
                name.set("")
                age.set("")
                gender.set("")
                Role.set("")
                password.set("")
                mail.set("")

            btnSub = Button(btn_frame, text="Insert", bg="#01a3a4", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=addData)
            btnSub.grid(row=0, column=0)

            btnUp = Button(btn_frame, text="Update", bg="#F79F1F", fg="white", width=6, padx=20, pady=5,
                           font=("times", 16, "bold"), command=updateData)
            btnUp.grid(row=0, column=1)

            btnDel = Button(btn_frame, text="Delete", bg="#ee5253", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=deleteData)
            btnDel.grid(row=0, column=2)

            btnClr = Button(btn_frame, text="Clear", bg="#1289A7", fg="white", width=6, padx=20, pady=5,
                            font=("times", 16, "bold"), command=clearData)
            btnClr.grid(row=0, column=3)

            myFrame = Frame(Frame1)
            myFrame.place(x=0, y=425, width=1920, height=500)

            style = ttk.Style()
            style.configure("Treeview", font=("times", 15), rowheight=38)
            style.configure("Treeview.Heading", font=("times", 16, "bold"))

            table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7))

            table.column("0", anchor=CENTER,width=70)
            table.column("1", stretch=NO, width=70)
            table.column("3", anchor=CENTER,width=70)
            table.column("6", anchor=CENTER,width=70)

            table.heading("0", text="S.NO")
            table.heading("1", text="ID")
            table.heading("2", text="Nom ")
            table.heading("3", text="AGE")
            table.heading("4", text="Genre")
            table.heading("5", text="mail")
            table.heading("6", text="Contact")
            table.heading("7", text="password")
            table["show"] = 'headings'
            table.bind("<ButtonRelease-1>", getrecord)
            table.pack(fill=X)

            fetchData()

        def GSM_Function():
            print("hydvdhfj")






        def Sc_Function():
            print("asjzdhfads")

        def MeTst_Function():
            print("MeTst_Function Works")

        def destroy():
            time.sleep(1)
            Window.destroy()


        def init_Home():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.75, rely=0.125, relheight=0.78, relwidth=0.23)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="1")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")

            Label2 = Label(Frame1)
            Label2.place(relx=0.2, rely=0.05, height=21, width=100)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''Team Member :''', anchor=N)


        EntryRecherche = Entry(Window)
        EntryRecherche.place(relx=0.182, rely=0.026, height=30, relwidth=0.221)
        EntryRecherche.configure(background="white")
        EntryRecherche.configure(disabledforeground="white", bd=0)
        EntryRecherche.configure(font="TkFixedFont")
        EntryRecherche.configure(highlightbackground = "white", highlightcolor= "white")
        EntryRecherche.configure(insertbackground="black")
        EntryRecherche.insert(0, 'Recherche')

        MesureTest = PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BTN/Btnadmin/Mesuretest.png")
        BMesureTest = Button(Window)
        BMesureTest.place(relx=0.02, rely=0.190, height=29, width=140)
        BMesureTest.configure(pady="0", bd=0)
        BMesureTest.configure(image=MesureTest)
        BMesureTest.configure(command=MeTst_Function)


        GSM = PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BTN/Btnadmin/Gsm.png")
        BGsm = Button(Window)
        BGsm.place(relx=0.02, rely=0.290, height=29, width=100)
        BGsm.configure(pady="0", bd=0)
        BGsm.configure(image=GSM)
        BGsm.configure(command=GSM_Function)

        ING = PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BTN/Btnadmin/Ing.png")
        BING = Button(Window)
        BING.place(relx=0.02, rely=0.390, height=29, width=100)
        BING.configure(pady="0", bd=0)
        BING.configure(image=ING)
        BING.configure(command=Ing_Function)

        TECH = PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BTN/Btnadmin/tech.png")
        BTECH = Button(Window)
        BTECH.place(relx=0.02, rely=0.490, height=29, width=100)
        BTECH.configure(pady="0", bd=0)
        BTECH.configure(image=TECH)
        BTECH.configure(command=Tech_Function)

        SECLT = PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BTN/Btnadmin/ServiceClient.png")
        BSECLT = Button(Window)
        BSECLT.place(relx=0.02, rely=0.590, height=36, width=140)
        BSECLT.configure(pady="0", bd=0)
        BSECLT.configure(image=SECLT)
        BSECLT.configure(command=Sc_Function)


        # créer un menu
        menubar = Menu(Window)
        # créer un sous-menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="GSM", command=GSM_Function)
        filemenu.add_command(label="Ing", command=Ing_Function)
        filemenu.add_command(label="Tech", command=Tech_Function)
        filemenu.add_command(label="quit",command=Window.quit)
        menubar.add_cascade(label="Managment", menu=filemenu)
        Window.config(menu=menubar)

        Window.mainloop()
    main_Manager()
