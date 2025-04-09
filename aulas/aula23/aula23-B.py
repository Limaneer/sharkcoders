from tkinter import *
import tkintermapview
from tkdial import Dial

def oooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="yellow", fill="yellow")
def ooooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="blue", fill="blue")
def oooooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="lime", fill="lime")
def ooooooo():
    map_widget.canvas.itemconfig(polygon1.canvas_polygon,outline="red", fill="red")
def d1():
    bragança_marker.set_position(d.get(),ds.get())
def d2():
    bragança_marker.set_position(d.get(),ds.get())
def oooooooo():
    bragança_marker.text = e.get()
    bragança_marker.set_position(d.get(),ds.get())

root = Tk()
root.title("teste")
root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)


button1 = Button(root, text= "amarelo",command=oooo)
button1.place( x=30, y=30)
button2 = Button(root, text= "azul",command=ooooo)
button2.place( x=30, y=60)
button3 = Button(root, text= "verde",command=oooooo)
button3.place( x=30, y=90)
button4 = Button(root, text= "vermelho",command=ooooooo)
button4.place( x=30, y=120)

d = Dial(root,start=-80,end=90,unit_color="black",color_gradient=("orange","red"),command=d1,text="y: ")
d.place(x=20, y=150)
ds = Dial(root,start=-180,end=180,unit_color="black",color_gradient=("orange","red"),command=d2, text="x: ")
ds.place(x=20, y=300)
e = Entry(root)
e.place(x=20, y=450)
button5 = Button(root, text= "confirmar",command=oooooooo)
button5.place( x=30, y=480)


map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600,corner_radius=0)

map_widget.set_position(39.81222,-7.99138)

polygon1 = map_widget.set_polygon([(41.9816058 ,-7.1628248),(41.9229751 ,-6.5401652),(41.6608612 ,-6.5621379),(41.5705121, -6.2325480),(41.2904514, -6.5401652),(41.2761913, -6.6962840),(41.0437270, -6.8489446),(41.0491329, -6.9610854),(40.8673065, -6.8542950),(40.5612782, -6.8623561),(40.5312800 ,-6.8122357),(40.4518276, -6.8640816),(40.3501991, -6.8021100),(40.2314058 ,-7.0417354),(40.1237576, -7.0328229),(40.0144602, -6.8900006),(39.7119325, -7.0541089),(39.6908007, -7.5759595),(39.1362600, -7.1976178),(39.0369241 ,-6.9833844),(38.4522547, -7.3624127),(38.1667408 ,-7.1097272),(38.1789844, -6.9833844),(38.0352086 ,-7.0240789),(38.0508341, -7.1042340),(38.0036963, -7.2660395),(37.5682097, -7.5474735),(37.2369451 ,-7.4436413),(37.0620450, -7.9231044),(37.1223439, -8.4747784),(37.0464046, -8.9142316),(37.5423970 ,-8.7654966),(37.9386167, -8.7986978),(38.3860190, -8.7735750),(38.4155889 ,-8.5626691),(38.5847282, -8.6951956),(38.4454879 ,-9.1765020),(38.6589506, -9.2364749),(38.6327403, -9.0515607),(38.7473297, -8.9499371),(38.6369265 ,-8.8805859),(38.7593895 ,-8.8726474),(38.8663958 ,-8.9687778),(38.8607458 ,-9.0795080),(38.7210594, -9.1351262),(38.7174585 ,-9.4480742),(39.3465032, -9.2987530),(40.8086103,-8.6011212),(41.8756572, -8.8428204),(42.1138832, -8.2249227),(41.8086688, -8.2111066),(41.8456831 ,-7.2058575)],fill_color = 'blue',name='yay',outline_color="blue")

bragança_marker = map_widget.set_marker(d.get(), ds.get())

map_widget.set_zoom(7)
map_widget.pack()
root.mainloop()
