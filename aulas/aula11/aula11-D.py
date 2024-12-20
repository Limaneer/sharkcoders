import math

ligada= True
lista = ["lista de operações:", "1-adicionar", "2-subtraír","3-multiplicar", "4-dividir","5-potenciar","6-off(desliga a calculadora)", "7-ac(apagar tudo)","8-factorial(só afeta o primeiro número)"]

while ligada == True:
    print("+---------------+")
    print("| +-----------+ |")
    print("| | BEEP BOOP | |")
    print("| +-----------+ |")
    print("| DEL | ** | AC |")
    print("| 7 | 8 | 9 | = |")
    print("| 4 | 5 | 6 | / |")
    print("| 1 | 2 | 3 | * |")
    print("| . | 0 | + | - |")
    print("+---------------+")
    n1 = float(input("Diz-me o número 1: "))
    n2 = float(input("Diz-me o número 2: "))
    for r in lista:
        print(r)
    h =input("Seleciona o número da operação. ")

    u = 0

    if h == "1":
        u = n1 + n2
    elif h == "2":
        u = n1 - n2
    elif h == "3":
        u = n1 * n2
    elif h == "4":
        if n2 == 0:
            print("número indefinido")
        else:
            u = n1 / n2
    elif h == "5":
        u = n1 ** n2
    elif h == "6":
        ligada = False
    elif h == "7":
        print ("apagado com sucesso")
    elif h == "8":
        if n1 > 0:
            u = math.factorial(n1)
        else:
            print("número tem de ser maior que zero")
    else:
        print("comando inválido")
    print(u)

    i = True

    if ligada == True:
        while i == True:
            b = input("voltar a usar?(Y/N) ").lower()
        if b == "y":
            i = False
        elif b == "n":
            i = False
            ligada = False
        else:
            print("comando inválido.")
