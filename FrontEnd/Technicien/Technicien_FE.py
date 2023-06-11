from tkinter import *
from tkinter import messagebox, ttk, simpledialog
import sqlite3
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class Technicien(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Manager Pannel")
        self.geometry(f"{920}x{500}")
        self.minsize(1341, 728)
        self.maxsize(1341, 728)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.db_connection = sqlite3.connect("/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db")
        self.create_table()

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0, minsize=200)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", text_font=("Roboto", -16))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Mesures", command=self.Mesure)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Réclamations",
                                                        command=self.Reclamation)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling)
        self.scaling_optionmenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        self.main_button_1 = customtkinter.CTkButton(self, fg_color="red", text="Quitter", border_width=2,
                                                     command=self.on_closing)
        self.main_button_1.grid(row=3, column=3, padx=(10, 20), pady=(10, 20), sticky="nsew")

        self.appearance_mode_optionmenu.set("Dark")
        self.scaling_optionmenu.set("100%")

    def create_table(self):
        query1 = """CREATE TABLE IF NOT EXISTS mesures (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        perte_paquets REAL,
                        gigue REAL,
                        latence REAL,
                        bande_passante REAL,
                        opinion_moyenne REAL,
                        localisation TEXT
                    )"""
        self.db_connection.execute(query1)
        self.db_connection.commit()

    def Mesure(self):
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

    def Reclamation(self):
        Frame1 = customtkinter.CTkFrame(self)
        Frame1.place(relx=0.14, rely=0.01, relheight=0.9, relwidth=0.85)


        title_label = customtkinter.CTkLabel(Frame1, text="Liste des Réclamations", text_font=("Roboto", -16), pady=20)
        title_label.grid(row=0, column=0)

        tree = ttk.Treeview(Frame1, columns=("Utilisateur", "Description", "Statut"), show="headings")
        tree.grid(row=1, column=0, pady=10)

        tree.heading("Utilisateur", text="Utilisateur")
        tree.heading("Description", text="Description")
        tree.heading("Statut", text="Statut")

        add_button = customtkinter.CTkButton(Frame1, text="Ajouter", command=lambda: self.add_complaint(tree))
        add_button.grid(row=2, column=0, pady=(0, 10))

        delete_button = customtkinter.CTkButton(Frame1, text="Supprimer", command=lambda: self.delete_rows(tree))
        delete_button.grid(row=3, column=0)

        query = "SELECT utilisateur, description, statut FROM reclamations"
        cursor = self.db_connection.execute(query)

        for row in cursor:
            tree.insert("", "end", values=row)

    def add_complaint(self, tree):
        utilisateur = simpledialog.askstring("Utilisateur", "Entrez l'utilisateur:")
        description = simpledialog.askstring("Description", "Entrez la description:")
        statut = simpledialog.askstring("Statut", "Entrez le statut:")

        if utilisateur and description and statut:
            query = f"INSERT INTO reclamations (utilisateur, description, statut) VALUES ('{utilisateur}', '{description}', '{statut}')"
            self.db_connection.execute(query)
            self.db_connection.commit()
            messagebox.showinfo("Succès", "La réclamation a été ajoutée avec succès.")
            tree.insert("", "end", values=(utilisateur, description, statut))
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def delete_rows(self, tree):
        selected_items = tree.selection()

        if not selected_items:
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins une réclamation à supprimer.")
            return

        confirmation = messagebox.askquestion("Confirmation",
                                              "Voulez-vous vraiment supprimer les réclamations sélectionnées ?")

        if confirmation == "yes":
            for item in selected_items:
                item_id = tree.item(item)["values"][0]
                query = f"DELETE FROM reclamations WHERE id = {item_id}"
                self.db_connection.execute(query)
                tree.delete(item)

            self.db_connection.commit()
            messagebox.showinfo("Succès", "Les réclamations sélectionnées ont été supprimées avec succès.")

    def on_closing(self):
        if messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
            self.db_connection.close()
            self.destroy()

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_spacing_scaling(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    technicien = Technicien()
    technicien.mainloop()
