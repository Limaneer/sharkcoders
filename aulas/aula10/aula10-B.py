rlista = []
sujeito = "h"
sujeito2 = "h"
ativo = True
comandos = ["Comandos:","-adicionar","-remover","-substituir","-ver lista","-sair (AVISO: lista será apagada)"]
while ativo == True:
    comando = str(input("Diz-me um comando (help: ver lista de comandos): ").lower())
    if comando == "help":
        for x in comandos:
            print(x)
    elif comando == "adicionar":
        sujeito = str(input("Nome da pessoa: ")).lower()
        lista.append(sujeito)
    elif comando == "ver lista":
        print()
        print("Lista:")
        print()
        for x in lista:
            print(f"-{x}")
        print()
    elif comando == "remover":
        sujeito = str(input("Nome da pessoa: ")).lower()
        if sujeito in lista:
            lista.remove(sujeito)
        else:
            print("Nome não existe na lista.")
    elif comando == "substituir":
        sujeito = str(input("Nome novo: ")).lower()
        sujeito2 = str(input("Nome antigo: ")).lower()
        if sujeito2 in lista:
            lista[(lista.index(sujeito2))] = sujeito
        else:
            print("Nome antigo não existe na lista.")
    elif comando == "sair":
        ativo = False
    else:
        print("Comando inválido, tente outra vez.")
