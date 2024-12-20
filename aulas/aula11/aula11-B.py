def yippie(temp):
    x = ((temp - 32) * (5/9))
    return x

s = float(input("temp em farenheit: "))

x = yippie(s)

print(f"temperatura em celsius: {x}")
