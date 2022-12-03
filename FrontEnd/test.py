1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
import tkinter
from tkintermapview import TkinterMapView

root_tk = tkinter.Tk()
root_tk.geometry(f"{600}x{400}")
root_tk.title("map_view_simple_example.py")

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# google normal tile server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_address("Wellington New Zealand", marker=True)

root_tk.mainloop()