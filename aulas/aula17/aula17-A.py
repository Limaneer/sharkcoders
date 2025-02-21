from tkinter import *
import random as random

root = Tk()

root.pont = 0
root.tempo = 30
root.jog = False

def tempo():
    if root.tempo > 0:
        root.after(1000, tempo)
        root.tempo = root.tempo - 1
        label6.config(text=f"  Tempo restante: {root.tempo} segundos")
    else:
        root.jog = False
def but1():
    if root.jog == True:
        
        button1.place_forget()
        x = random.randint(55,390)
        y = random.randint(45,180)
        button1.place(width=60, height= 60, x=x, y=y)
        root.pont = root.pont + 1
        label5.config(text=f"Pontuação: {root.pont}")
def but2():
    if root.jog == False:
        root.pont = 0
        root.tempo = 30
        label6.config(text=f"  Tempo restante: {root.tempo} segundos")
        label5.config(text=f"Pontuação: {root.pont}")

        tempo()

    root.jog = True

root.title("hunting game")
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)

button1 = Button(root, command=but1 , text=":D",font="arial 14 bold")
button1.place(width=60, height= 60, x=216.5, y = 120)
button2 = Button(root, command=but2 , text="Começar",font="arial 14 bold")
button2.place(width=120, height= 60, x=186.5, y = 285)

label1 = Label(root, text="+------------------------------------------------------------------+", font="arial 14 bold")
label1.place( x=40, y = 20)
label2 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label2.place( x=43, y = 40)
label3 = Label(root, text="+------------------------------------------------------------------+", font="arial 14 bold")
label3.place( x=40, y = 240)
label4 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label4.place( x=450, y = 40)
label5 = Label(root, text="Pontuação: 0", font="arial 14 bold")
label5.place( x=330, y = 0)
label6 = Label(root, text="  Tempo restante: 30 segundos", font="arial 14 bold")
label6.place( x=30, y = 0)

root.mainloop()
