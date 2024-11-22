palavra = (input("vou fazer uma placa, diz-me o que deve dizer:  ")).upper()
d = (str(input("com que cara(se é feliz, :); se é triste :(; chateada, >:(; se é malvada, >:); se está muito feliz, :D; se não tem, N)?  "))).upper()


print("  +---+")
print("--|   |")
for x in palavra:
    print(f"  | {x} |")

if d == ":)":
    print("  |   |")
    print("  |. .|")
    print("--|\_/|")
    print("  +---+")



if d == ":D":
    print("  |   |")
    print("  |. .|")
    print("  |___|")
    print("--|\_/|")
    print("  +---+")



elif d == ":(":
    print("  |   |")
    print("  |. .|")
    print("--|/‾\|")
    print("  +---+")



elif d == ">:(":
    print("  |   |")
    print("  |`V´|")
    print("  |. .|")
    print("--|/‾\|")
    print("  +---+")



elif d == ">:)":
    print("  |   |")
    print("  |`V´|")
    print("  |. .|")
    print("--|\_/|")
    print("  +---+")



elif d == "N":
    print("--|   |")
    print("  +---+")
