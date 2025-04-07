from tkinter import *
import tkintermapview

def oooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="yellow", fill="yellow")
def ooooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="blue", fill="blue"
                                                                              "")
root = Tk()
root.title("teste")
root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)


button1 = Button(root, text= "yay",command=oooo)
button1.place( x=30, y=30)
button2 = Button(root, text= "-yay",command=ooooo)
button2.place( x=30, y=60)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600,corner_radius=0)

map_widget.set_position(39.81222,-7.99138)

polygon1 = map_widget.set_polygon([(41.9588073, -7.1565780),(42.9588073, -7.1565780),(42.9588073, -6.1565780),(41.9588073, -6.1565780)],fill_color = 'blue',name='yay',outline_color="blue")

bragança_marker = map_widget.set_marker(41.7810877,-6.7768625, text="Casa XPTO")

map_widget.set_zoom(7)
map_widget.pack()
root.mainloop()
