import random
import sys


print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print("a água evaporou e por isso ninguém consegue beber")
nome = input("decidiram que tu, (diz o teu nome) ")
print("serás a melhor pessoa para ir desviver o rei de tudo que é mau, que aceita comer cupcakes com mustarda, o senhor evaporaáguaparatematar (prefiro o nome eaptm)")
print("começas a tua aventura, mas menos do que 4 minutos depois encontras o teu primeiro obstáculo!")
print("o caminho separa-se em duas direções:")
print("1.Direita")
print("2.Esquerda")
direcao = int(input("Em que direção vais? "))

if direcao == 1:
    print("Decides ir para a direita e entras na floresta encantada...")
elif direcao == 2:
    print("Decides ir para a esquerda, mas escolheste mal! Encontras-te deparado com a ponte mais flácida do mundo!")
    input("Tens 50% de chance de atravessares com sucesso. Queres passar pela ponte?(S/N) ")
    print("Querendo ou não, tu atravessa-la")
    e = random.randint(1,2)
    if e == 1:
        print("Conseguiste! Procedes para a floresta encantada.")
    elif e==2:
        print("A ponte morre e tu partes com ela.")
        sys.exit(0)

print("ao entrar na floresta, encontras um baú com moedas")
moni = random.randint(1,20)
print(f"Conseguiste {moni} moedas! :D!")
print("procedes e eventualmente entras dentro de uma casinha até que o chão procede a si plesmente parar de existir e começas a \ncair a altas velocidades, felizmente estás treinado em acrobática e não te magoas ao aterrar")
print("infelizmente ao fundo está um guardião que diz:")
print("-Estou a pensar num número entre 1 e 20. com 5 tentativas consegues adivinhá-lo?")
tent = 5
numi = random.randint(1,20)
while True:
    tent = tent - 1
    if tent >= 0:
        g = int(input("Diz um número: "))
        if g == numi:
            print("adivinhas-te! podes proceder.")
            break
        elif g > numi:
            print("Errado, o número é menor")
        elif g < numi:
            print("Errado, o número é maior")


    else:
        print("-acabaram as tentativas")
        print("procedes a parar de existir")
        sys.exit(0)

print("esperando uma batalha dolorosa, demoras horas a prepararte e depois, entras.")
print("no meio do chão há uma formiga")
print("enquanto procuras eaptm sem querer pisas nela")
print(f"PARABÉNS, {nome}, com eaptm morto, finalmente começa a chover e todagente começa a beber água diáriamente.")
