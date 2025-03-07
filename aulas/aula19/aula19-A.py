from tkinter import *
import random as random
import random
from unicodedata import normalize


lista2 = ["amor","fato","vies","voce","mito","como","caos","esmo","brio","vide","sede","pois","apos","vida","casa","medo","saga","auge","onus","vovo","ermo","sina","alem","suma","pela","mais","mote","tolo","urge","idem","zelo","crer","tudo","apto","veio","pude","amar","ruim","area","para","rude","sera","coxo","doce","ater","cota","soar","tras","fase","ente","logo","auto","deus","voga","alma","onde","pelo","arte","sido","jugo","ante","cedo","rima","meio","traz","numa","meta","isso","sela","cujo","noia","sair","cela","teor","face","asco","alvo","nojo","foco","odio","alto","pose","agir","base","vale","teve","todo","ocio","eita","rito","irao","novo","agil","alva","tese","bojo","quer","nada","alta"]
lista = []
for x in lista2:
    y = normalize('NFKD', x).encode('ASCII','ignore').decode('ASCII')
    lista.append(y)



root = Tk()
root.win = 0
root.mal = []
root.e1 = "_"
root.e2 = "_"
root.e3 = "_"
root.e4 = "_"
root.q1 = False
root.q2 = False
root.q3 = False
root.q4 = False

root.l1 = ""
root.l2 = ""
root.l3 = ""
root.l4 = ""

root.t = 0

root.word = random.choice(lista)
root.ded = False
root.vidas = 6
root.adivinha=""

for x in root.word:
    root.t = root.t + 1

    if root.t == 1:
        root.l1 = x
    elif root.t == 2:
        root.l2 = x
    elif root.t == 3:
        root.l3 = x
    elif root.t == 4:
        root.l4 = x


def but1():
    lista2 = ["amor","fato","viés","você","mito","como","caos","esmo","brio","ação","vide","sede","pois","após","vida","casa","medo","saga","auge","ônus","vovó","ermo","sina","além","suma","pela","mais","mote","tolo","urge","idem","zelo","crer","tudo","apto","veio","pude","amar","ruim","área","para","rude","será","coxo","doce","ater","cota","soar","trás","fase","ente","logo","auto","deus","voga","alma","onde","pelo","arte","sido","jugo","ante","cedo","rima","meio","traz","numa","meta","isso","sela","cujo","noia","sair","cela","teor","face","asco","alvo","nojo","foco","ódio","alto","pose","agir","base","vale","teve","todo","ócio","eita","rito","irão","novo","ágil","alva","tese","bojo","quer","nada","alta"]
    lista = []
    for x in lista2:
        y = normalize('NFKD', x).encode('ASCII','ignore').decode('ASCII')
        lista.append(y)

    root.win = 0
    root.mal = []
    root.e1 = "_"
    root.e2 = "_"
    root.e3 = "_"
    root.e4 = "_"
    root.l1 = ""
    root.l2 = ""
    root.l3 = ""
    root.l4 = ""
    root.t = 0
    root.word = random.choice(lista)
    root.ded = False
    root.vidas = 6
    root.adivinha=""
    label6.config(text = "+----+   \n|        \n|        \n|        \n|        \n#########")
    label7.config(text=f"Palavra: {root.e1}{root.e2}{root.e3}{root.e4}")
    label8.config(text=f"Letras erradas:\n {root.mal}")
    for x in root.word:
        root.t = root.t + 1

        if root.t == 1:
            root.l1 = x
        elif root.t == 2:
            root.l2 = x
        elif root.t == 3:
            root.l3 = x
        elif root.t == 4:
            root.l4 = x

    root.q1 = False
    root.q2 = False
    root.q3 = False
    root.q4 = False


def but2():



    root.adivinha = Letra.get()
    root.adivinha = Letra.get()

    if root.adivinha == root.l1 and root.q1 == False:
        root.e1 = root.l1
        root.win = root.win + 1
        root.q1 = True

    if root.adivinha == root.l2 and root.q2 == False:
        root.e2 = root.l2
        root.win = root.win + 1
        root.q2 = True

    if root.adivinha == root.l3 and root.q3 == False:
        root.e3 = root.l3
        root.win = root.win + 1
        root.q3 = True

    if root.adivinha == root.l4 and root.q4 == False:
        root.e4 = root.l4
        root.win = root.win + 1
        root.q4 = True

    if root.adivinha not in (root.l1, root.l2, root.l3, root.l4):
        root.mal.append(root.adivinha)
        root.x = root.vidas
        root.vidas = root.x - 1

    if root.win == 4:
        label7.config(text=f"Palavra: {root.e1}{root.e2}{root.e3}{root.e4}")
        label6.config(text="Ganhaste :D!!!")

    else:


        if root.vidas == 6:
            label6.config(text = "+----+   \n|        \n|        \n|        \n|        \n#########")

        elif root.vidas == 5:
            label6.config(text ="+----+   \n |    O   \n|        \n|        \n|        \n#########")

        elif root.vidas == 4:
            label6.config(text= "+----+   \n |    O   \n|    |   \n|        \n|        \n#########")

        elif root.vidas == 3:
            label6.config(text= "+----+   \n |    O   \n|   /|   \n|        \n|        \n#########")

        elif root.vidas == 2:
            label6.config(text= "+----+   \n |    O   \n|   /|\  \n|        \n|        \n#########")

        elif root.vidas == 1:
            label6.config(text= "+----+   \n |    O   \n|   /|\  \n|     \  \n|        \n#########")

        elif root.vidas == 0:
            label6.config(text = f"+----+   \n |    O   \n|   /|\  \n|   / \  \n|        \n#########\nperdeste\na palavra era {root.word}")

        label7.config(text=f"Palavra: {root.e1}{root.e2}{root.e3}{root.e4}")
        label8.config(text=f"Letras erradas:\n {root.mal}")

    Letra.delete(0, END)


root.title("Jogo da forca")
root.geometry("500x400+400+100")
root.wm_resizable(width=False,height=False)


button2 = Button(root, command=but2 , text="Adivinhar",font="arial 14 bold")
button2.place(width=120, height= 60, x=186.5, y = 285)
button1 = Button(root, command=but1 , text="Recomeçar",font="arial 14 bold")
button1.place(width=120, height= 60, x=306.5, y = 285)

label1 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold")
label1.place( x=40, y = 20)
label2 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label2.place( x=63, y = 40)
label3 = Label(root, text="    +-----------------------------------------------------------+", font="arial 14 bold")
label3.place( x=40, y = 260)
label4 = Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font="arial 14 bold")
label4.place( x=430, y = 40)
Letra = Entry(root)
Letra.place( x=185, y = 350)
label6 = Label(root, text="+----+   \n|        \n|        \n|        \n|        \n#########", font="arial 14 bold")
label6.place( x=80, y = 80)

label7 = Label(root, text="Palavra:____", font="arial 14 bold")
label7.place( x=220, y = 80)

label8 = Label(root, text="Letras erradas:", font="arial 14 bold")
label8.place( x=220, y = 120)

root.mainloop()
