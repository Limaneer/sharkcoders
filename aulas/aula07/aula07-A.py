
#                                            detetor de preço de energia


inst = (input("tipo de instalação(R para residências, I para industrias e C para comércio):  ")).upper()  #+-----input
kwh = float(input("insira kwh:  "))                                                                       #+

if kwh < 0:             #-+
    print(":|")         # |
    h = kwh             # +----detetor de n.º negativos
    kwh = h * -1        #-+


if inst == "R":                     #-+
    if kwh <= 500:                  # |
        p = 0.40 * kwh              # |
    elif kwh > 500:                 # |
        p = 0.65 * kwh              # |
elif inst == "C":                   # |
    if kwh <= 1000:                 # |
        p = 0.55 * kwh              # +----definir o preço
    elif kwh > 1000:                # |
        p = 0.60 * kwh              # |
elif inst == "I":                   # |
    if kwh <= 5000:                 # |
        p = 0.55 * kwh              # |
    elif kwh > 5000:                # |
        p = 0.60 * kwh              #-+
else:                                      #+
    print(":|")                            #+------detetor de inputs inválidos
    p = 0                                  #+

a = p                              #+
p = round(a, 2)                    #+-----arredondar com 2 casas decimais

print(f"o preço é {p} euros")              #output
