from tkinter import *
import sys
import os

tamanho = 100

root = Tk()

root.numero=0

def bu1():
    if button1.digit == "q":
        root.numero = root.numero + 1

    if root.numero % 2 == 0 and button1.digit == "q":
        button1.config(text="X")
        button1.digit = "X"
    elif button1.digit == "q":
        button1.config(text="O")
        button1.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu2():
    if button2.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button2.digit == "q":
        button2.config(text="X")
        button2.digit = "X"
    elif button2.digit == "q":
        button2.config(text="O")
        button2.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu3():
    if button3.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button3.digit == "q":
        button3.config(text="X")
        button3.digit = "X"
    elif button3.digit == "q":
        button3.config(text="O")
        button3.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu4():
    if button4.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button4.digit == "q":
        button4.config(text="X")
        button4.digit = "X"
    elif button4.digit == "q":
        button4.config(text="O")
        button4.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu5():
    if button5.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button5.digit == "q":
        button5.config(text="X")
        button5.digit = "X"
    elif button5.digit == "q":
        button5.config(text="O")
        button5.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu6():
    if button6.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button6.digit == "q":
        button6.config(text="X")
        button6.digit = "X"
    elif button6.digit == "q":
        button6.config(text="O")
        button6.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu7():
    if button7.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button7.digit == "q":
        button7.config(text="X")
        button7.digit = "X"
    elif button7.digit == "q":
        button7.config(text="O")
        button7.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu8():
    if button8.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button8.digit == "q":
        button8.config(text="X")
        button8.digit = "X"
    elif button8.digit == "q":
        button8.config(text="O")
        button8.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu9():
    if button9.digit == "q":
        root.numero = root.numero + 1
    if root.numero % 2 == 0 and button9.digit == "q":
        button9.config(text="X")
        button9.digit = "X"
    elif button9.digit == "q":
        button9.config(text="O")
        button9.digit = "O"

    if button1.digit == "X" and button2.digit == "X" and button3.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button4.digit == "X" and button5.digit == "X" and button6.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button7.digit == "X" and button8.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button4.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button2.digit == "X" and button5.digit == "X" and button8.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button6.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "X" and button5.digit == "X" and button9.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button3.digit == "X" and button5.digit == "X" and button7.digit == "X":
        indicador1.config(text="X ganhou!!!")

    elif button1.digit == "O" and button2.digit == "O" and button3.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button4.digit == "O" and button5.digit == "O" and button6.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button7.digit == "O" and button8.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button4.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button2.digit == "O" and button5.digit == "O" and button8.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button6.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button1.digit == "O" and button5.digit == "O" and button9.digit == "O":
        indicador1.config(text="O ganhou!!!")

    elif button3.digit == "O" and button5.digit == "O" and button7.digit == "O":
        indicador1.config(text="O ganhou!!!")
def bu10():
    button1.config(text="")
    button1.digit = "q"
    button2.config(text="")
    button2.digit = "q"
    button3.config(text="")
    button3.digit = "q"
    button4.config(text="")
    button4.digit = "q"
    button5.config(text="")
    button5.digit = "q"
    button6.config(text="")
    button6.digit = "q"
    button7.config(text="")
    button7.digit = "q"
    button8.config(text="")
    button8.digit = "q"
    button9.config(text="")
    button9.digit = "q"
    indicador1.config(text="")
    root.numero = 0



root.title("jogo do galo :D")
root.geometry("580x350+400+100")
root.wm_resizable(width=False,height=False)

indicador1 = Label(root, text="",font="arial 12 bold")
indicador1.place(x=140, y=0)

button1 = Button(root, command=bu1, text="",font="arial 14 bold")
button1.place(width=tamanho, height=tamanho, x=40, y = 20)
button1.digit = "q"

button2 = Button(root, command=bu2,text="",font="arial 14 bold")
button2.place(width=tamanho, height=tamanho, x=140, y = 20)
button2.digit = "q"

button3 = Button(root, command=bu3,text="",font="arial 14 bold")
button3.place(width=tamanho, height=tamanho, x=240, y = 20)
button3.digit = "q"

button4 = Button(root, command=bu4,text="",font="arial 14 bold")
button4.place(width=tamanho, height=tamanho, x=40, y = 120)
button4.digit = "q"

button5 = Button(root, command=bu5, text="",font="arial 14 bold")
button5.place(width=tamanho, height=tamanho, x=140, y = 120)
button5.digit = "q"

button6 = Button(root, command=bu6,text="",font="arial 14 bold")
button6.place(width=tamanho, height=tamanho, x=240, y = 120)
button6.digit = "q"

button7 = Button(root, command=bu7,text="",font="arial 14 bold")
button7.place(width=tamanho, height=tamanho, x=40, y = 220)
button7.digit = "q"

button8 = Button(root, command=bu8,text="",font="arial 14 bold")
button8.place(width=tamanho, height=tamanho, x=140, y = 220)
button8.digit = "q"

button9 = Button(root, command=bu9,text="",font="arial 14 bold")
button9.place(width=tamanho, height=tamanho, x=240, y = 220)
button9.digit = "q"

button10 = Button(root, command=bu10,text="recomeçar",font="arial 14 bold")
button10.place(width=tamanho, height=tamanho, x=440, y = 120)


root.mainloop()
