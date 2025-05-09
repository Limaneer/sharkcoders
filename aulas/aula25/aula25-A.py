from tkinter import *

root = Tk()
root.title("Window")
root.geometry("346x475")
root.resizable(width=False,height=False)


#--Buttons
b1 = Button(root, text="", height=30, width=46, borderwidth=10, bg="red")
b1.place(x=0,y=0)
b1["state"] = "disabled"
b2 = Button(root, text="", height=4, width=46, borderwidth=10, bg="red")
b2.place(x=0,y=0)
b2["state"] = "disabled"
b3 = Button(root, text="Pokedex", height=4, width=10, borderwidth=10, bg="red",disabledforeground="yellow")
b3.place(x=0,y=0)
b3["state"] = "disabled"
b6 = Button(root, text="", height=1, width=20, borderwidth=10, bg="red", relief="sunken")
b6.place(x=155,y=20)
b6["state"] = "disabled"
b4 = Entry(root, width=24, bg="khaki3")
b4.place(x=164,y=31)
l1 = Label(root, text="Name:", font=("Courier",12), bg="red")
l1.place(x=97,y=27)

b5 = Button(root, text="", height=13, width=30, borderwidth=10, bg="red",relief="sunken")
b5.place(x=55,y=90)
b5["state"] = "disabled"

b7 = Button(root, text="", height=13, width=30, borderwidth=2, bg="khaki3")
b7.place(x=64,y=98)
b7["state"] = "disabled"
root.mainloop()
