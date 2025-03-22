from tkinter import *
import random


def ded():
    label7.config(text="Morreu :(")
    root.ded = True
def win():
    if root.pont == 20:
        label7.config(text="Ganhou :)")
        root.ded = True
    label9.config(text=f"Pontuação = {root.pont}/20")


def but1():
    if root.ded == False:
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




def but2():
    if root.ded == False:
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


def but3():
    if root.ded == False:
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


def but4():
    if root.ded == False:
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


def but5():
    if root.ded == False:
        if root.coory == root.maxcoory and root.coorx == root.maxcoorx:
            if root.coory < root.encoory:
                root.encoory = root.encoory - 15
                label6.place(x=root.encoorx, y=root.encoory)
            if root.coorx > root.encoorx:
                root.encoorx = root.encoorx + 15
                label6.place(x=root.encoorx, y=root.encoory)
            if root.coory > root.encoory:
                root.encoory = root.encoory + 15
                label6.place(x=root.encoorx, y=root.encoory)
            if root.coorx < root.encoorx:
                root.encoorx = root.encoorx - 15
                label6.place(x=root.encoorx, y=root.encoory)

            root.pont = root.pont + 1

            win()
    if root.coory == root.encoory and root.coorx == root.encoorx:
        ded()


def but6():
    root.pont = 0
    root.ded = False
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
    label7.config(text="                 ")
    label5.place(x=root.coorx, y=root.coory)
    label6.place(x=root.encoorx, y=root.encoory)
    label9.config(text="Pontuação = 0/20")


def main(event):
    if event.char == "w":
        but2()
    if event.char == "a":
        but3()
    if event.char == "d":
        but4()
    if event.char == "s":
        but1()
    if event.char == " ":
        but5()


root = Tk()

root.pont = 0
root.ded = False
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
root.configure(background='grey29')
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)


button2 = Button(root , text=r" /\ " ,font="arial 14 bold", command=but2, bg="black", fg="white")
button2.place(width=30, height= 30, x=135, y = 300)
button1 = Button(root , text="\/",font="arial 14 bold", command=but1, bg="black", fg="white")
button1.place(width=30, height= 30, x=135, y = 360)
button3 = Button(root , text="<",font="arial 16", command=but3, bg="black", fg="white")
button3.place(width=30, height= 30, x=105, y = 330)
button4 = Button(root , text=">",font="arial 16", command=but4, bg="black", fg="white")
button4.place(width=30, height= 30, x=165, y = 330)
button5 = Button(root , text="0",font="arial 16", command=but5, bg="black", fg="white")
button5.place(width=30, height= 30, x=135, y = 330)
button6 = Button(root , text="Recomeçar",font="arial 16", command=but6, bg="black", fg="white")
button6.place(width=120, height= 30, x=235, y = 330)

label1 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold", bg="grey29")
label1.place( x=40, y = 20)
label2 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold", bg="grey29")
label2.place( x=63, y = 40)
label4 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold", bg="grey29")
label4.place( x=427, y = 40)
label3 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold", bg="grey29")
label3.place( x=40, y = 267)
label5 = Label(root, text="'v'", font="arial 14 bold", bg="blue")
label5.place( x= root.strtcoorx, y = root.strtcoory)
label6 = Label(root, text="`^´", font="arial 14 bold", bg="red")
label6.place( x= root.maxcoorx, y = root.maxcoory)
label7 = Label(root, text="                 ", fg="white", font="arial 14 bold", bg="black")
label7.place( x= 300, y =0)
label8 = Label(root, text=" O ", font="arial 14 bold", bg = "lime")
label8.place( x= root.maxcoorx, y = root.maxcoory)
label9 = Label(root, text="Pontuação = 0/20", font="arial 14 bold", bg="black", fg="white")
label9.place( x=90, y = 0)


root.bind('<KeyPress>', main)

root.mainloop()
