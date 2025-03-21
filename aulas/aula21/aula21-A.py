from tkinter import *
import random


def ded():
    label7.config(text="Morreu :(")
def win():
    label7.config(text="Ganhou :)")


def but1():
    if root.coory != root.maxcoory:
        root.coory = root.coory + 30
        label5.place(x= root.coorx, y = root.coory)

        if root.coory < root.encoory:
            root.encoory = root.encoory - 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx > root.encoorx:
            root.encoorx = root.encoorx + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coory > root.encoory:
            root.encoory = root.encoory + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx < root.encoorx:
            root.encoorx = root.encoorx - 15
            label6.place(x= root.encoorx, y = root.encoory)

    if root.coory == root.encoory and root.coorx == root.encoorx:
        ded()
    elif root.coory == root.maxcoory and root.coorx == root.maxcoorx:
        win()



def but2():
    if root.coory != root.mincoory:
        root.coory = root.coory - 30
        label5.place(x= root.coorx, y = root.coory)



        if root.coory < root.encoory:
            root.encoory = root.encoory - 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx > root.encoorx:
            root.encoorx = root.encoorx + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coory > root.encoory:
            root.encoory = root.encoory + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx < root.encoorx:
            root.encoorx = root.encoorx - 15
            label6.place(x= root.encoorx, y = root.encoory)

    if root.coory == root.encoory and root.coorx == root.encoorx:
        ded()
    elif root.coory == root.maxcoory and root.coorx == root.maxcoorx:
        win()

def but3():
    if root.coorx != root.mincoorx:
        root.coorx = root.coorx - 30
        label5.place(x= root.coorx, y = root.coory)

        if root.coory < root.encoory:
            root.encoory = root.encoory - 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx > root.encoorx:
            root.encoorx = root.encoorx + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coory > root.encoory:
            root.encoory = root.encoory + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx < root.encoorx:
            root.encoorx = root.encoorx - 15
            label6.place(x= root.encoorx, y = root.encoory)

    if root.coory == root.encoory and root.coorx == root.encoorx:
        ded()
    elif root.coory == root.maxcoory and root.coorx == root.maxcoorx:
        win()

def but4():
    if root.coorx != root.maxcoorx:
        root.coorx = root.coorx + 30
        label5.place(x= root.coorx, y = root.coory)

        if root.coory < root.encoory:
            root.encoory = root.encoory - 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx > root.encoorx:
            root.encoorx = root.encoorx + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coory > root.encoory:
            root.encoory = root.encoory + 15
            label6.place(x= root.encoorx, y = root.encoory)
        if root.coorx < root.encoorx:
            root.encoorx = root.encoorx - 15
            label6.place(x= root.encoorx, y = root.encoory)

    if root.coory == root.encoory and root.coorx == root.encoorx:
        ded()
    elif root.coory == root.maxcoory and root.coorx == root.maxcoorx:
        win()

def main(event):
    if event.char == "w":
        but2()
    if event.char == "a":
        but3()
    if event.char == "d":
        but4()
    if event.char == "s":
        but1()


root = Tk()



root.coorx = 70
root.coory = 40
root.mincoorx = 70
root.mincoory = 40
root.maxcoorx = 400
root.maxcoory = 250
root.strtcoorx = 70
root.strtcoory = 40
root.encoorx = 400
root.encoory = 250
root.enmincoorx = 70
root.enmincoory = 40
root.enmaxcoorx = 400
root.enmaxcoory = 250
root.enstrtcoorx = 400
root.enstrtcoory = 250
root.en = 0



root.title("Jogo")
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)


button2 = Button(root , text=r" /\ " ,font="arial 14 bold", command=but2)
button2.place(width=30, height= 30, x=235, y = 300)
button1 = Button(root , text="\/",font="arial 14 bold", command=but1)
button1.place(width=30, height= 30, x=235, y = 360)
button3 = Button(root , text="<",font="arial 16", command=but3)
button3.place(width=30, height= 30, x=205, y = 330)
button4 = Button(root , text=">",font="arial 16", command=but4)
button4.place(width=30, height= 30, x=265, y = 330)
button5 = Button(root , text="0",font="arial 16")
button5.place(width=30, height= 30, x=235, y = 330)

label1 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold")
label1.place( x=40, y = 20)
label2 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label2.place( x=63, y = 40)
label4 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label4.place( x=427, y = 40)
label3 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold")
label3.place( x=40, y = 267)
label5 = Label(root, text="'v'", font="arial 14 bold", bg="blue")
label5.place( x= root.strtcoorx, y = root.strtcoory)
label6 = Label(root, text="`^´", font="arial 14 bold", bg="red")
label6.place( x= root.maxcoorx, y = root.maxcoory)
label7 = Label(root, text="", font="arial 10 bold")
label7.place( x= 200, y =10)
label8 = Label(root, text=" O ", font="arial 14 bold", bg = "lime")
label8.place( x= root.maxcoorx, y = root.maxcoory)

root.bind('<KeyPress>', main)

root.mainloop()
