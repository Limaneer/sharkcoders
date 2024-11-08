inst = (input("tipo de instalação(R para residências, I para industrias e C para comércio):  ")).upper()
kwh = float(input("insira kwh:  "))

if kwh < 0:
    print(":|")
    h = kwh
    kwh = h * -1


if inst == "R":
    if kwh <= 500:
        p = 0.40 * kwh
    elif kwh > 500:
        p = 0.65 * kwh
elif inst == "C":
    if kwh <= 1000:
        p = 0.55 * kwh
    elif kwh > 1000:
        p = 0.60 * kwh
elif inst == "I":
    if kwh <= 5000:
        p = 0.55 * kwh
    elif kwh > 5000:
        p = 0.60 * kwh
else:
    print(":|")
    p = "69.420"

print(f"o preço é {p} euros")
