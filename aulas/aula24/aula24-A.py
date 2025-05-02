import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def buscar_piada():
    url = "https://api.chucknorris.io/jokes/random"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        piada = dados["value"]
        imagem_url = dados["icon_url"]

        # atualizar texto
        texto_piada.config(text=piada)

        # bucar imagem
        imagem_resposta = requests.get(imagem_url)
        imagem_bytes = BytesIO(imagem_resposta.content)
        imagem_pil = Image.open(imagem_bytes)

        # redimensionar imagem
        imagem_pil = imagem_pil.resize((100,100))

        # converter para tkinter
        imagem_tk = ImageTk.PhotoImage(imagem_pil)

        #atualizar imagem no label
        imagem_label.config(image=imagem_tk)
        imagem_label.image = imagem_tk

    else:
        texto_piada.config(text="Erro ao buscar piada!")

# criar janela
janela = tk.Tk()
janela.title("Piadas do Chuck  Norris")

#imagem label
imagem_label = tk.Label(janela)
imagem_label.pack(pady=10)

# texto da piada
texto_piada = tk.Label(janela, text="Clica no botao para ver uma piada!", wraplength=400, justify="left", padx=10, pady=10)
texto_piada.pack()

#botao
botao = tk.Button(janela, text=" Buscar nova piada", command=buscar_piada)
botao.pack(pady=10)

janela.mainloop()
