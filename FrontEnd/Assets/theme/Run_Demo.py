import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("test")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("1000 x 700")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "proxttk.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk")

d = tk.IntVar(value=2)  
# Entry
entryf = ttk.Entry(custom_widget)
entryf.insert(0, "test entry")
entryf.grid(row=2, column=2, padx=(0.5,05), pady=(.5,0.5), sticky="ew")
# Create a Frame 
hhh = ttk.LabelFrame(custom_widget, text="sudbgsdf", padding=1)
hhh.grid(row=1, column=1, padx=(.3,0.3), pady=(0.3,0.3), sticky="nsew") 
g = tk.DoubleVar(value=75.0)
prog = ttk.Progressbar(custom_widget, value=100, variable=g, mode="determinate")
prog.grid(row=4, column=4, padx=(0.4,0.4), pady=(0.4,0.4), sticky="ew")

g = tk.DoubleVar(value=75.0)
sliderr = ttk.Scale(custom_widget, from_=100, to=0, variable=g, command=lambda event: g.set(sliderr.get()))
sliderr.grid(row=6, column=6, padx=(0.7,0.7), pady=(0.7,0.7), sticky="ew") 

root.mainloop()