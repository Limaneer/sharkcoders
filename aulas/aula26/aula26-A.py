from tkinter import *
from tkinter import PhotoImage
import requests
from PIL import Image, ImageTk
from io import BytesIO

root = Tk()
root.title("Window")
root.geometry("346x475")
root.resizable(width=False,height=False)
root.nome= ""
root.url = f""
root.p = ""
root.t = ""
root.a = ""
image = PhotoImage(file="img.png")


def pesquisar():
    nome = b4.get()
    root.url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    root.resp = requests.get(root.url)
    print(root.resp.status_code)
    if root.resp.status_code == 200:
        root.dados= root.resp.json()
        root.n = root.dados["name"]
        print(root.n)
        root.t = root.dados["types"][0]["type"]["name"]
        root.a = root.dados["height"]/10
        root.p = root.dados["weight"]/10
        iurl = root.dados["sprites"]["other"]["official-artwork"]["front_default"]
        iresp = requests.get(iurl)
        print(iresp)
        i = Image.open(BytesIO(iresp.content)).resize((200, 200))
        it = ImageTk.PhotoImage(i)
        l7.config(image=it, width = 210 , height= 200 )
        l7.image=it
        b11.config(text = f"Peso: {root.p}")
        b12.config(text = f"Tipo: {root.t}")
        b13.config(text = f"Altura: {root.a}")

#--Buttons
b1 = Button(root, text="", height=30, width=46, borderwidth=10, bg="red")
b1.place(x=0,y=0)
b1["state"] = "disabled"
b2 = Button(root, text="", height=4, width=46, borderwidth=10, bg="red")
b2.place(x=0,y=0)
b2["state"] = "disabled"
b3 = Button(root, height=65, width=70, borderwidth=10, bg="red",disabledforeground="",image=image)
b3.place(x=0,y=0)
b3["state"] = "disabled"
b6 = Button(root, text="", height=1, width=20, borderwidth=10, bg="red", relief="sunken")
b6.place(x=155,y=20)
b6["state"] = "disabled"
b4 = Entry(root, width=24, bg="khaki3")
b4.place(x=164,y=31)
l1 = Label(root, text="Nome:", font=("Courier",12), bg="red")
l1.place(x=97,y=27)

b5 = Button(root, text="", height=13, width=30, borderwidth=10, bg="red",relief="sunken")
b5.place(x=55,y=90)
b5["state"] = "disabled"

l7 = Label(root, text="", height=13, width=30, bg="khaki3")
l7.place(x=65,y=100)


b8 = Button(root, text="pesquisar", bg="red", command=pesquisar)
b8.place(x=140,y=320)

b9 = Button(root, text="", height=6, width=46, borderwidth=10, bg="red")
b9.place(x=0,y=360)
b9["state"] = "disabled"
b10 = Button(root, height=1, width=10, borderwidth=10, bg="red", text= "Informações:", disabledforeground="black")
b10.place(x=0,y=360)
b10["state"] = "disabled"
b11 = Button(root, height=1, width=10, borderwidth=10, bg="red", text= f"Peso:  {root.p}", disabledforeground="black")
b11.place(x=250,y=360)
b11["state"] = "disabled"
b12 = Button(root, height=1, width=10, borderwidth=10, bg="red", text= f"Tipo:  {root.t}", disabledforeground="black")
b12.place(x=155,y=402)
b12["state"] = "disabled"
b13 = Button(root, height=1, width=10, borderwidth=10, bg="red", text= f"Altura:  {root.a}", disabledforeground="black")
b13.place(x=250,y=402)
b13["state"] = "disabled"
root.mainloop()
