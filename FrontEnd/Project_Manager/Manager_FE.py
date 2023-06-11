from tkinter import *
from tkinter import messagebox, ttk
import customtkinter
from BackEnd.Services.TechnicienService import *
from BackEnd.Services.IngineerService import *
from BackEnd.Services.ServiceClientService import *
from tkintermapview import TkinterMapView


customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

dbTech = TechnicienService("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")
dbIng = IngineerService("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")
dbSCS = ServiceClientService("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Manager Pannel")
        self.geometry(f"{920}x{500}")
        self.minsize(1341, 728)
        self.maxsize(1341, 728)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0, minsize=200)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", text_font=("Roboto", -16))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Mesure Test Drive", command=self.MeTst_Function)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Site GSM", command=self.GSM_Function)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="G.Ingenieurs", command=self.Ing_Function)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="G.Technicien", command=self.Tech_Function)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="G.Service Client", command=self.Sc_Function)
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))


        self.main_button_1 = customtkinter.CTkButton(self, fg_color="red",text="Quiter", border_width=2,command=self.on_closing)
        self.main_button_1.grid(row=3, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def Tech_Function(self):
        print("Tech Works")
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.98, relwidth=0.85)


        name = StringVar()
        age = StringVar()
        gender = StringVar()
        mail = StringVar()
        Role = StringVar()
        password = StringVar()

        frame1 = customtkinter.CTkFrame(Frame1, padx=20, pady=20)
        frame1.pack(side=TOP, fill=X)

        lblTitle = customtkinter.CTkLabel(frame1, pady=10)
        lblTitle.grid(columnspan=2)

        lblName = customtkinter.CTkLabel(frame1, text="Nom ", pady=10)
        lblName.grid(row=1, column=0)

        txtName = customtkinter.CTkEntry(frame1, textvariable=name, width=200)
        txtName.grid(row=1, column=1)

        lblAge = customtkinter.CTkLabel(frame1, text="Age",  pady=10)
        lblAge.grid(row=2, column=0)

        txtAge = customtkinter.CTkEntry(frame1, textvariable=age, width=200)
        txtAge.grid(row=2, column=1)

        lblgen = customtkinter.CTkLabel(frame1, text="Genre", pady=10)
        lblgen.grid(row=3, column=0)

        cb = ttk.Combobox(frame1, width=41, textvariable=gender, state="readonly")
        cb['values'] = ("Male", "Female", "Others")
        cb.grid(row=3, column=1)

        lblAdd = customtkinter.CTkLabel(frame1, text="Mail", pady=10)
        lblAdd.grid(row=4, column=0)

        txtAdd = customtkinter.CTkEntry(frame1, width=200, textvariable=mail)
        txtAdd.grid(row=4, column=1)

        lblCon = customtkinter.CTkLabel(frame1, text="Role", pady=10)
        lblCon.grid(row=5, column=0)

        txtCon = customtkinter.CTkEntry(frame1, textvariable=Role, width=200)
        txtCon.grid(row=5, column=1)
        txtCon.insert(0, "Technicien")
        txtCon.configure(state=DISABLED)

        lblMail = customtkinter.CTkLabel(frame1, text="password", pady=10)
        lblMail.grid(row=6, column=0)

        txtMail = customtkinter.CTkEntry(frame1, textvariable=password, width=200)
        txtMail.grid(row=6, column=1)

        btn_frame = customtkinter.CTkFrame(frame1)
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

        btnSub = customtkinter.CTkButton(btn_frame, text="Insert", width=6, padx=20, pady=5,
                       command=addData)
        btnSub.grid(row=0, column=0)

        btnUp = customtkinter.CTkButton(btn_frame, text="Update", width=6, padx=20, pady=5,
                       command=updateData)
        btnUp.grid(row=0, column=1)

        btnDel = customtkinter.CTkButton(btn_frame, text="Delete", width=6, padx=20, pady=5,
                         command=deleteData)
        btnDel.grid(row=0, column=2)

        btnClr = customtkinter.CTkButton(btn_frame, text="Clear", width=6, padx=20, pady=5,
                        command=clearData)
        btnClr.grid(row=0, column=3)

        myFrame = customtkinter.CTkFrame(Frame1)
        myFrame.place(x=0, y=425, width=1920, height=500)

        style = ttk.Style()
        style.configure("Treeview", font=("times", 15), rowheight=38)
        style.configure("Treeview.Heading", font=("times", 16, "bold"))

        table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7))

        table.column("0", anchor=CENTER, width=70)
        table.column("1", stretch=NO, width=70)
        table.column("3", anchor=CENTER, width=70)
        table.column("6", anchor=CENTER, width=70)

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

    def Ing_Function(self):
        print("Ing Works")
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.98, relwidth=0.85)

        name = StringVar()
        age = StringVar()
        gender = StringVar()
        mail = StringVar()
        Role = StringVar()
        password = StringVar()

        frame1 = customtkinter.CTkFrame(Frame1, padx=20, pady=20)
        frame1.pack(side=TOP, fill=X)

        lblTitle = customtkinter.CTkLabel(frame1, text="Gestion", pady=10)
        lblTitle.grid(columnspan=2)

        lblName = customtkinter.CTkLabel(frame1, text="Nom ", pady=10)
        lblName.grid(row=1, column=0)

        txtName = customtkinter.CTkEntry(frame1, textvariable=name,  width=200)
        txtName.grid(row=1, column=1)

        lblAge = customtkinter.CTkLabel(frame1, text="Age", pady=10)
        lblAge.grid(row=2, column=0)

        txtAge = customtkinter.CTkEntry(frame1, textvariable=age, width=200)
        txtAge.grid(row=2, column=1)

        lblgen = customtkinter.CTkLabel(frame1, text="Genre",pady=10)
        lblgen.grid(row=3, column=0)

        cb = ttk.Combobox(frame1, width=41, textvariable=gender, state="readonly", font=("times", 16))
        cb['values'] = ("Male", "Female", "Others")
        cb.grid(row=3, column=1)

        lblAdd = customtkinter.CTkLabel(frame1, text="mail",pady=10)
        lblAdd.grid(row=4, column=0)

        txtAdd = customtkinter.CTkEntry(frame1, width=200, textvariable=mail)
        txtAdd.grid(row=4, column=1)

        lblCon = customtkinter.CTkLabel(frame1, text="Role", pady=10)
        lblCon.grid(row=5, column=0)

        txtCon = customtkinter.CTkEntry(frame1,  textvariable=Role, width=200)
        txtCon.grid(row=5, column=1)
        txtCon.insert(0, "Ingineer")
        txtCon.configure(state=DISABLED)

        lblMail = customtkinter.CTkLabel(frame1, text="mot de passe", pady=10)
        lblMail.grid(row=6, column=0)

        txtMail = customtkinter.CTkEntry(frame1, textvariable=password, width=200)
        txtMail.grid(row=6, column=1)

        btn_frame = customtkinter.CTkFrame(frame1, )
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

        btnSub = customtkinter.CTkButton(btn_frame, text="Insert", width=6, padx=20, pady=5,
                         command=addData)
        btnSub.grid(row=0, column=0)

        btnUp = customtkinter.CTkButton(btn_frame, text="Update", width=6, padx=20, pady=5,
                        command=updateData)
        btnUp.grid(row=0, column=1)

        btnDel = customtkinter.CTkButton(btn_frame, text="Delete", width=6, padx=20, pady=5,
                         command=deleteData)
        btnDel.grid(row=0, column=2)

        btnClr = customtkinter.CTkButton(btn_frame, text="Clear", width=6, padx=20, pady=5,
                         command=clearData)
        btnClr.grid(row=0, column=3)

        myFrame = customtkinter.CTkFrame(Frame1)
        myFrame.place(x=0, y=425, width=1920, height=500)

        style = ttk.Style()
        style.configure("Treeview", font=("times", 15), rowheight=38)
        style.configure("Treeview.Heading", font=("times", 16, "bold"))

        table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7))

        table.column("0", anchor=CENTER, width=70)
        table.column("1", stretch=NO, width=70)
        table.column("3", anchor=CENTER, width=70)
        table.column("6", anchor=CENTER, width=70)

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

    def Sc_Function(self):
        print("Sc_Function Works")
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.98, relwidth=0.85)

        age = StringVar()
        gender = StringVar()
        mail = StringVar()
        Role = StringVar()
        password = StringVar()

        frame1 = customtkinter.CTkFrame(Frame1, padx=20, pady=20)
        frame1.pack(side=TOP, fill=X)

        lblTitle = customtkinter.CTkLabel(frame1, text="Gestion", pady=10)
        lblTitle.grid(columnspan=2)

        lblName = customtkinter.CTkLabel(frame1, text="Nom ", pady=10)
        lblName.grid(row=1, column=0)

        txtName = customtkinter.CTkEntry(frame1, width=200)
        txtName.grid(row=1, column=1)

        lblAge = customtkinter.CTkLabel(frame1, text="Age", pady=10)
        lblAge.grid(row=2, column=0)

        txtAge = customtkinter.CTkEntry(frame1, textvariable=age, width=200)
        txtAge.grid(row=2, column=1)

        lblgen = customtkinter.CTkLabel(frame1, text="Genre", pady=10)
        lblgen.grid(row=3, column=0)

        cb = ttk.Combobox(frame1, width=40, textvariable=gender, state="readonly", font=("times", 16))
        cb['values'] = ("Male", "Female", "Others")
        cb.grid(row=3, column=1)

        lblAdd = customtkinter.CTkLabel(frame1, text="mail",  pady=10)
        lblAdd.grid(row=4, column=0)

        txtAdd = customtkinter.CTkEntry(frame1, width=200, textvariable=mail)
        txtAdd.grid(row=4, column=1)

        lblCon = customtkinter.CTkLabel(frame1, text="Role", pady=10)
        lblCon.grid(row=5, column=0)

        txtCon = customtkinter.CTkEntry(frame1, textvariable=Role, width=200)
        txtCon.grid(row=5, column=1)
        txtCon.insert(0, "Client_Service")
        txtCon.configure(state=DISABLED)

        lblMail = customtkinter.CTkLabel(frame1, text="mot de passe", pady=10)
        lblMail.grid(row=6, column=0)

        txtMail = customtkinter.CTkEntry(frame1,  textvariable=password, width=200)
        txtMail.grid(row=6, column=1)

        btn_frame = customtkinter.CTkFrame(frame1)
        btn_frame.grid(row=7, column=1, columnspan=4)

        def fetchData():
            table.delete(*table.get_children())
            count = 0
            for row in dbSCS.fetch_record():
                count += 1
                table.insert("", END, values=(count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        def addData():
            if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                messagebox.showinfo("Message", "Please Fill All Records")
            else:
                dbSCS.insert(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get())
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Insert Successfully")

        def getrecord(event):
            srow = table.focus()
            data = table.item(srow)
            global row
            row = data['values']
            age.set(row[3])
            gender.set(row[4])
            Role.set(row[6])
            password.set(row[7])
            mail.set(row[5])

        def updateData():
            if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or cb.get() == "" or txtCon.get() == "" or txtMail.get() == "":
                messagebox.showinfo("Message", "Please Fill All Records")
            else:
                dbSCS.update_record(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtMail.get(),
                                    (row[1]))
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Update Successfully")

        def deleteData():
            dbSCS.remove_record(row[1])
            fetchData()
            clearData()
            messagebox.showinfo("Message", "Record Delete Successfully")

        def clearData():
            age.set("")
            gender.set("")
            Role.set("")
            password.set("")
            mail.set("")

        btnSub = customtkinter.CTkButton(btn_frame, text="Insert", width=6, padx=20, pady=5,
                         command=addData)
        btnSub.grid(row=0, column=0)

        btnUp = customtkinter.CTkButton(btn_frame, text="Update", width=6, padx=20, pady=5,
                        command=updateData)
        btnUp.grid(row=0, column=1)

        btnDel = customtkinter.CTkButton(btn_frame, text="Delete", width=6, padx=20, pady=5,
                         command=deleteData)
        btnDel.grid(row=0, column=2)

        btnClr = customtkinter.CTkButton(btn_frame, text="Clear", width=6, padx=20, pady=5,
                         command=clearData)
        btnClr.grid(row=0, column=3)

        myFrame = customtkinter.CTkFrame(Frame1)
        myFrame.place(x=0, y=425, width=1920, height=500)

        style = ttk.Style()
        style.configure("Treeview", font=("times", 15), rowheight=38)
        style.configure("Treeview.Heading", font=("times", 16, "bold"))

        table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7))

        table.column("0", anchor=CENTER, width=70)
        table.column("1", stretch=NO, width=70)
        table.column("3", anchor=CENTER, width=70)
        table.column("6", anchor=CENTER, width=70)

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

    def GSM_Function(self):
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.98, relwidth=0.85)
        map_widget = TkinterMapView(Frame1, width=600, height=400, corner_radius=0)
        map_widget.pack(fill="both", expand=True)
        # google normal tile server
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        map_widget.set_address("Kairouan Tunisie", marker=True)

    def MeTst_Function(self):
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.9, relwidth=0.85)

        frame1 = customtkinter.CTkFrame(Frame1, padx=20, pady=20)
        frame1.pack(side=TOP, fill=X)

        labels = ["La perte de paquets", "La gigue", "La latence", "La bande passante",
                  "La note d'opinion moyenne",
                  "Localisation"]
        entries = []

        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(frame1, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = customtkinter.CTkEntry(frame1)
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries.append(entry)

        measure_button = customtkinter.CTkButton(Frame1, text="Mesurer", command=lambda: self.measure_action(entries))
        measure_button.place(relx=0.4, rely=0.9, anchor="center")


    def measure_action(self, entries):
        values = [entry.get() for entry in entries]

        # Calculate coverage state based on a threshold value
        threshold = 10  # Adjust the threshold value as needed
        coverage_state = "Mauvaise" if float(values[0]) > threshold else "Bonne"

        # Display the values and coverage state in a dialog box
        messagebox.showinfo("Mesure des paramètres QoS",
                            f"Perte de paquets: {values[0]}\nGigue: {values[1]}\nLatence: {values[2]}\n"
                            f"Bande passante: {values[3]}\nÉtat de la couverture: {coverage_state}")
        self.store_measurement(values)


    def store_measurement(self, values):
        query = """INSERT INTO mesures (perte_paquets, gigue, latence, bande_passante, opinion_moyenne, localisation)
                           VALUES (?, ?, ?, ?, ?, ?)"""
        self.db_connection.execute(query, values)
        self.db_connection.commit()
        messagebox.showinfo("Mesure des paramètres QoS", "Mesure enregistrée avec succès")

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_spacing_scaling(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_closing(self, event=0):
        exit_command = messagebox.askyesno("Exit", "Are you sure you want to exit")
        if exit_command > 0:
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

