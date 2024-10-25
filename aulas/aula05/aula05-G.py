from random import randint

n = int(input("tenta adivinhar um nº entre 1-5: "))

n2 = randint(1,5)

if n2 == n:
    print("acertaste!")
else:
    print("falhaste!")
    print("o valor é:")
    print(n2)

