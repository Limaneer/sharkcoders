import tkinter as Tk
from tkinter import messagebox



def yippie(n):
    messagebox.showerror("Title", "Message")
    a = []
    for i in range (10):
        if (n>1):
            a.append(yippie(n-1))
        else:
            a.append(i)
    return a

def yay():
    print(yippie(100))
    print(yippie(100))
    print(yippie(100))
    print(yippie(100))
    print(yippie(100))
    while True:
        messagebox.showinfo("Title", "Message")

root = Tk.Tk()

root.title("Jogo da morte")
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)

button2 = Tk.Button(root, command=yay , text="Yippie",font="arial 14 bold")
button2.place(width=120, height= 60, x=190, y = 170)

root.mainloop()
