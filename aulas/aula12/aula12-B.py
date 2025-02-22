import random
from unicodedata import normalize

lista2 = ["amor","fato","viés","você","mito","como","caos","esmo","brio","ação","vide","sede","pois","após","vida","casa","medo","saga","auge","ônus","vovó","ermo","sina","além","suma","pela","mais","mote","tolo","urge","idem","zelo","crer","tudo","apto","veio","pude","amar","ruim","área","para","rude","será","coxo","doce","ater","cota","soar","trás","fase","ente","logo","auto","deus","voga","alma","onde","pelo","arte","sido","jugo","ante","cedo","rima","meio","traz","numa","meta","isso","sela","cujo","noia","sair","cela","teor","face","asco","alvo","nojo","foco","ódio","alto","pose","agir","base","vale","teve","todo","ócio","eita","rito","irão","novo","ágil","alva","tese","bojo","quer","nada","alta"]

lista = []
for x in lista2:
    y = normalize('NFKD', x).encode('ASCII','ignore').decode('ASCII')
    lista.append(y)

word = random.choice(lista)

win = 0

mal = []

e1 = "_"
e2 = "_"
e3 = "_"
e4 = "_"

l1 = ""
l2 = ""
l3 = ""
l4 = ""

t = 0

for x in word:
    t = t + 1

    if t == 1:
        l1 = x
    elif t == 2:
        l2 = x
    elif t == 3:
        l3 = x
    elif t == 4:
        l4 = x

ded = False
vidas = 6
while not ded:



    if vidas == 6:
        print("+----+   ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("#########")
    elif vidas == 5:
        print("+----+   ")
        print("|    O   ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("#########")
    elif vidas == 4:
        print("+----+   ")
        print("|    O   ")
        print("|    |   ")
        print("|        ")
        print("|        ")
        print("#########")
    elif vidas == 3:
        print("+----+   ")
        print("|    O   ")
        print("|   /|   ")
        print("|        ")
        print("|        ")
        print("#########")
    elif vidas == 2:
        print("+----+   ")
        print("|    O   ")
        print("|   /|\  ")
        print("|        ")
        print("|        ")
        print("#########")
    elif vidas == 1:
        print("+----+   ")
        print("|    O   ")
        print("|   /|\  ")
        print("|     \  ")
        print("|        ")
        print("#########")
    elif vidas == 0:
        print("+----+   ")
        print("|    O   ")
        print("|   /|\  ")
        print("|   / \  ")
        print("|        ")
        print("#########")
        print("perdeste")
        print(f"a palavra era {word}")
        break

    print(f"Palavra: {e1}{e2}{e3}{e4}")
    print(f"Letras erradas: {mal}")
    adivinha = input("Diz-me uma letra ").lower()

    if adivinha == l1:
        e1 = l1
        win = win + 1

    if adivinha == l2:
        e2 = l2
        win = win + 1

    if adivinha == l3:
        e3 = l3
        win = win + 1

    if adivinha == l4:
        e4 = l4
        win = win + 1

    if adivinha not in (l1, l2, l3, l4):
        print("ERRADO!!")
        mal.append(adivinha)
        x = vidas
        vidas = x - 1
