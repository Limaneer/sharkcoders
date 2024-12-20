e = str(input("Diz-me uma frase: "))
r = str(input("Diz-me a letra a verificar:  "))
y = 0
def nletras(frase,letra):
    k = 0
    l = 0
    for p in frase:
        if p == letra:
            l = k
            k = l + 1
    return k
y = nletras(e,r)
if y > 0:
    print(f"a letra {r} está presente {y} vezes")
else:
    print(f"a letra {r} não está presente")
