import random
parar = False
while parar == False:
    num = random.randint(1,100)
    l = True
    print("estou a pensar num número de 1 a 100, tenta adivinhá-lo")
    resp = int(input("Diz um número: "))
    mai = ("h")
    win = False
    ten = 0
    pert = ("h")
    if resp == num:
        print("Ganhaste de primeira!!!")
        print("Parabéns!!")
    else:
        while win == False:
            if num == resp:
                win == True
                print(f"Ganhaste com {ten} tentativas !!")
                break
            else:
                if num-resp < 15 and num-resp > -15:
                    pert = ("perto")
                else:
                    pert = ("longe")

                if num-resp > 0:
                    mai = ("maior")
                elif num-resp < 0:
                    mai = ("menor")
                resp = int(input(f"Falhaste! Estás {pert} do número, ele é {mai}, tenta de novo: "))
                ten = ten + 1


    while l == True:
        ttt= (input("Queres jogar de novo(Y/N)?  ")).upper()
        if ttt == "Y":
            parar = False
            l = False
        elif ttt == "N":
            parar = True
            l = False
        else:
            print("Podes dar-me uma resposta a sério?")


