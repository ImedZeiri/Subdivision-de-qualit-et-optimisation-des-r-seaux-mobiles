import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

from PIL import ImageTk


class Manager:
    def main_Manager():
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
        Window.bind("<Configure>", resize_image)

        def Home_Function():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")


        def GSM_Function():
            print("GSM Works")
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")

            Label2 = Label(Frame1)
            Label2.place(relx=0.05, rely=0.198, height=21, width=100)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''GSM :''', anchor=W)

        def Ing_Function():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(background="white")

            notebook = ttk.Notebook(Frame1)
            notebook.configure
            notebook.place(relx=0.01, rely=0.0125, relheight=0.81, relwidth=0.6558)
            frame1 = Frame(notebook, width=400, height=280)
            frame1.configure(background="white")
            frame2 = Frame(notebook, width=400, height=280)
            frame2.configure(background="white")
            frame1.pack(fill='both', expand=True)
            frame2.pack(fill='both', expand=True)
            notebook.add(frame1, text='Ajouter Ingenieur')
            notebook.add(frame2, text='Voir list')
            print("Ing_Function Works")

            # Label & Entry for name
            lblName = Label(frame1, text="Email : ")
            lblName.place(x=10, y=10)
            entryEmail = Entry(frame1)
            entryEmail.place(x=100, y=10, width=200)


            # Label & Entry Email
            lblEmail = Label(frame1, text="Nom")
            lblEmail.place(x=10, y=40)
            entryNom = Entry(frame1)
            entryNom.place(x=100, y=40, width=200)

            # Label & Entry Age
            lblAge = Label(frame1, text="Prenom")
            lblAge.place(x=10, y=70)
            entryPrenom = Entry(frame1)
            entryPrenom.place(x=100, y=70, width=200)

            # Label & Entry Age
            lblAge = Label(frame1, text="Mot de passe")
            lblAge.place(x=10, y=100)
            entryMdp = Entry(frame1)
            entryMdp.place(x=100, y=100, width=200)

            def RecupererData():
                DataIngineer = [entryEmail.get(),entryNom.get(),entryPrenom.get(),entryMdp.get(),"Ingineer"]
                from BackEnd.DB_Intializer.Db import Db_Connexion
                from BackEnd.Services.Add_Service import Add
                Add.Add_Ing(DataIngineer)

            btnValidate = Button(frame1, text="Valider",command=RecupererData)
            btnValidate.place(x=100, y=130, width=200, height=25)

        def Tech_Function():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(background="white")

            notebook = ttk.Notebook(Frame1)
            notebook.configure
            notebook.place(relx=0.01, rely=0.0125, relheight=0.81, relwidth=0.6558)
            frame1 = Frame(notebook, width=400, height=280)
            frame1.configure(background="white")
            frame2 = Frame(notebook, width=400, height=280)
            frame2.configure(background="white")
            frame1.pack(fill='both', expand=True)
            frame2.pack(fill='both', expand=True)
            notebook.add(frame1, text='Ajouter Ingenieur')
            notebook.add(frame2, text='Voir list')
            print("Tech_Function Works")

            # Label & Entry for name
            lblName = Label(frame1, text="Email : ")
            lblName.place(x=10, y=10)
            entryEmail = Entry(frame1)
            entryEmail.place(x=100, y=10, width=200)


            # Label & Entry Email
            lblEmail = Label(frame1, text="Nom")
            lblEmail.place(x=10, y=40)
            entryNom = Entry(frame1)
            entryNom.place(x=100, y=40, width=200)

            # Label & Entry Age
            lblAge = Label(frame1, text="Prenom")
            lblAge.place(x=10, y=70)
            entryPrenom = Entry(frame1)
            entryPrenom.place(x=100, y=70, width=200)

            # Label & Entry Age
            lblAge = Label(frame1, text="Mot de passe")
            lblAge.place(x=10, y=100)
            entryMdp = Entry(frame1)
            entryMdp.place(x=100, y=100, width=200)

            def RecupererData():
                DataTech = [entryEmail.get(),entryNom.get(),entryPrenom.get(),entryMdp.get(),"Technicien"]
                from BackEnd.DB_Intializer.Db import Db_Connexion
                from BackEnd.Services.Add_Service import Add
                Add.Add_Tech(DataTech)

            btnValidate = Button(frame1, text="Valider",command=RecupererData)
            btnValidate.place(x=100, y=130, width=200, height=25)


        def Sc_Function():
            print("Sc_Function Works")

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
