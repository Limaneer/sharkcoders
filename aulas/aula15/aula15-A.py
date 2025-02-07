from threading import Thread

from tkinter import *
from tkinter.ttk import *

import os
import time
root = Tk()



def AAAA():
    while True:
        #Thread(target=AAAA).start()
        time.sleep(1)
        new_window = Toplevel(root)
        new_window.title("Nova janela")



root.title("yay")
root.geometry("500x300+200+200")
root.wm_resizable(width = False, height = False)

button1 = Button(root, text = ":D", command=AAAA)
button1.pack(pady=10)


label1 = Label(root, text = "fbhhfhbrgtrgturtbborgtbbbbbbbbbbbbbbbbbbgggbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
label1.place(width=800, height=20, x=00, y=100)
label2 = Label(root, text = "botãozinho amigável^")
label2.place(width=800, height=20, x=-210, y=50)

root.mainloop()
