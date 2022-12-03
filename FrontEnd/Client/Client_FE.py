from tkinter import *
from datetime import datetime
from time import strftime
from PIL import ImageTk


class Client:
    def main(self):
        Window = Tk()
        Window.title("Client")
        Window.geometry("1301x728")
        Window.minsize(1301, 728)
        Window.maxsize(1301, 728)
        bg = ImageTk.PhotoImage(file="/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/bgC1.png")
        canvas = Canvas(Window, width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_image(5, 0, image=bg, anchor='nw')
        def resize_image(e):
            global image, resized, image2
            image = Image.open("/Users/macbookpro/desktop/PFE_MOUNA/FrontEnd/Assets/bgC1.png")
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')
        Window.bind("<Configure>")


        Sub = Entry(Window)
        Sub.place(relx=0.35, rely=0.05, relheight=0.12, relwidth=0.300)

        Rec_Content = Text(Window)
        Rec_Content.place(relx=0.3, rely=0.4, relheight=0.38, relwidth=0.405)

        Frame1 = Frame(Window)
        Frame1.place(relx=0.78, rely=0.08, relheight=0.15, relwidth=0.2)
        Frame1.configure(relief='solid')
        Frame1.configure(borderwidth="0")
        Frame1.configure(relief="solid")
        Frame1.configure(background="Black")

        def Horloge():
            a = datetime.today().strftime('%A')
            b = (a.upper())
            c = (b[0:2])

            # Mechenism
            def time():
                a = strftime('%H : %M : %S')  # %H   %M   %S
                l1.config(text=a)
                l1.after(1000, time)

            l1 = Label(Frame1, font=('Century Gothic', 20),
                       bg='#0e1013',
                       foreground='#d3d3d3')

            l1.place(x=30, y=55)
            time()

            l2 = Label(Frame1, font=('Century Gothic', 20),
                       bg='#0e1013',
                       foreground='#d3d3d3')
            l2.config(text=c + " |")
            l2.place(x=30, y=15)
        Horloge()


        def AddReclamation():
            sub = Sub.get()
            content = Rec_Content.get("1.0", "end")
            from BackEnd.Services.AddReclamationService import AddReclamationService
            AddReclamationService.Add_Rec(sub,content)
            print(sub)
            print(content)



        BTN = Button(Window)
        BTN.place(relx=0.45, rely=0.85, height=30, width=120)
        BTN.configure(text="Envoyer")
        BTN.configure(activeforeground="#000000")
        BTN.configure(background="#d9d9d9")
        BTN.configure(disabledforeground="#a3a3a3")
        BTN.configure(foreground="#000000")
        BTN.configure(highlightbackground="#d9d9d9")
        BTN.configure(highlightcolor="black",border=0)
        BTN.configure(pady="0")
        BTN.configure(command=AddReclamation)


        def Destroy():
            Window.destroy()

        Window.mainloop()

    main(self=True)
