from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import customtkinter

class Technicien:
    def main(self):
        Window = Tk()
        Window.title("Technicien")
        Window.geometry("1301x728")
        Window.minsize(1301, 728)
        Window.maxsize(1301, 728)
        bg = ImageTk.PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BgTech.png")

        style = ttk.Style(Window)
        # Import the tcl file
        Window.tk.call("source", "/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/theme/proxttk.tcl")

        # Set the theme with the theme_use method
        style.theme_use("proxttk")

        d = tk.IntVar(value=2)

        canvas = Canvas(Window, width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_image(5, 0, image=bg, anchor='nw')
        canvas.create_image(0, 0, image=bg, anchor='nw')

        def resize_image(e):
            global image, resized, image2
            image = Image.open("/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/BgTech.png")
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')

        def Destroy():
            Window.destroy()
        def Mesure():
            Frame1 = Frame(Window)
            Frame1.place(relx=0.3, rely=0.275, relheight=0.51, relwidth=0.4558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")


            Labelframe12 = LabelFrame(Frame1)
            Labelframe12.place(relx=0.012, rely=0.0, relheight=0.099
                               , relwidth=0.285)
            Labelframe12.configure(relief='solid')
            Labelframe12.configure(foreground="black")
            Labelframe12.configure(text='''QoS (qualité de service)''')
            Labelframe12.configure(background="white")

            Label1 = Label(Frame1)
            Label1.place(relx=0.089, rely=0.203, height=21, width=150)
            Label1.configure(background="white")
            Label1.configure(disabledforeground="#a3a3a3")
            Label1.configure(foreground="#000000")
            Label1.configure(text='''La perte de paquets''', anchor=W)

            Label2 = Label(Frame1)
            Label2.place(relx=0.089, rely=0.303, height=21, width=150)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''La gigue''', anchor=W)

            Label3 = Label(Frame1)
            Label3.place(relx=0.089, rely=0.403, height=21, width=150)
            Label3.configure(background="white")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(foreground="#000000")
            Label3.configure(text='''La latence''', anchor=W)

            Label4 = Label(Frame1)
            Label4.place(relx=0.089, rely=0.503, height=21, width=150)
            Label4.configure(background="white")
            Label4.configure(disabledforeground="#a3a3a3")
            Label4.configure(foreground="#000000")
            Label4.configure(text='''La bande passante''', anchor=W)

            Label5 = Label(Frame1)
            Label5.place(relx=0.092, rely=0.603, height=21, width=160)
            Label5.configure(background="white")
            Label5.configure(disabledforeground="#a3a3a3")
            Label5.configure(foreground="#000000")
            Label5.configure(text='''La note d'opinion moyenne''', anchor=W)

            Label6 = Label(Frame1)
            Label6.place(relx=0.092, rely=0.703, height=21, width=150)
            Label6.configure(background="white")
            Label6.configure(disabledforeground="#a3a3a3")
            Label6.configure(foreground="#000000")
            Label6.configure(text='''Localisation ''', anchor=W)

            Entry1 = ttk.Entry(Frame1)
            Entry1.place(relx=0.385, rely=0.203, height=20, relwidth=0.198)

            Entry2 = ttk.Entry(Frame1)
            Entry2.place(relx=0.385, rely=0.303, height=20, relwidth=0.198)

            Entry3 = ttk.Entry(Frame1)
            Entry3.place(relx=0.385, rely=0.403, height=20, relwidth=0.198)

            Entry4 = ttk.Entry(Frame1)
            Entry4.place(relx=0.385, rely=0.503, height=20, relwidth=0.198)

            Entry5 = ttk.Entry(Frame1)
            Entry5.place(relx=0.385, rely=0.603, height=20, relwidth=0.191)

            Entry6 = ttk.Entry(Frame1)
            Entry6.place(relx=0.385, rely=0.703, height=20, relwidth=0.198)

            def DataRec():
                ppT = Entry1.get()
                gigue = Entry2.get()
                latence = Entry3.get()
                Bp = Entry4.get()
                NopMoy = Entry5.get()
                location = Entry6.get()
                if int(ppT)>10:
                    print("red")
                else:
                    print("vert")



            Window.BTNValide = ttk.Button(Frame1,style="AccentButton")
            Window.BTNValide.place(relx=0.5, rely=0.8, height=30, width=110)
            Window.BTNValide.configure(text="Mesures")
            Window.BTNValide.configure(command=DataRec)



        def Maintenance():
            print("Works")


        Window.BTNMeusure = customtkinter.CTkButton(Window)
        Window.BTNMeusure.place(relx=0.09459, rely=0.327, height=30, width=110)
        Window.BTNMeusure.configure(text="Mesures")
        Window.BTNMeusure.configure(command=Mesure)



        Window.BTNMaintenance = customtkinter.CTkButton(Window)
        Window.BTNMaintenance.place(relx=0.09459, rely=0.427, height=30, width=110)
        Window.BTNMaintenance.configure(text="Maintenance")
        Window.BTNMaintenance.configure(command=Maintenance)


        Window.bind("<Configure>", resize_image)
        Window.mainloop()

    main(self=True)

