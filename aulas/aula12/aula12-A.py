import random


while True:
    print("#######################################")
    print("#####         PEDRA         o     #####")
    print("#####        PAPEL          []    #####")
    print("#####       TESOURA         8<    #####")
    print("#######################################")
    print("#####                             #####")
    print("#####   1.JOGAR        2.sair     #####")
    print("#####                             #####")
    print("#######################################")
    play = int(input("Opção: "))
    if play == 2:
        break
    elif play == 1:
        escolhacomputador = int(random.randint(1,3))
        print("escolhe uma jogada:")
        print("1.Pedra")
        print("2.Papel")
        print("3.Tesoura")
        escolha = int(input("Escolhe um número:"))

        if escolhacomputador == 1:
            texto = "Pedra"
        elif escolhacomputador == 2:
            texto = "Papel"
        elif escolhacomputador == 3:
            texto = "Tesoura"

        if escolha == 1:
            texto2 = "Pedra"
        elif escolha == 2:
            texto2 = "Papel"
        elif escolha == 3:
            texto2 = "Tesoura"
        else:
            texto2 = ""
            print("escolha inválida")
            continue

        print(f"Escolha do computador: {texto}")
        print(f"Sua escolha: {texto2}")
        if escolhacomputador == escolha:
            print("Empate!!!")
        elif escolhacomputador == 1 and escolha == 2:
            print("Ganhou!!!!")
        elif escolhacomputador == 2 and escolha == 3:
            print("Ganhou!!!!")
        elif escolhacomputador == 3 and escolha == 1:
            print("Ganhou!!!!")
        elif escolhacomputador == 2 and escolha == 1:
            print("Perdeu!!")
        elif escolhacomputador == 3 and escolha == 2:
            print("Perdeu!!")
        elif escolhacomputador == 1 and escolha == 3:
            print("Perdeu!!")
    else:
        print("opção inválida")
