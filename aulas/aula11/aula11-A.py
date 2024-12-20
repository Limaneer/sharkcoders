x = 0

u = 0

r = 0

t = 0
print("move-te com wasd")
while True:
    e = str(input()).lower()
    if e == "w":
        f = r
        r = f + 1
    elif e == "s":
        f = r
        r = f - 1
    elif e == "d":
        f = t
        t = f + 1
    elif e == "a":
        f = t
        t = f - 1
    else:
        f = x
        x = f

    if x < 0:
        x = 0




    if r > 0:
        u = r
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

    print(("   " * t),"0")

    while u > 0:
        print("   " * t)
        y = u
        u = y - 1

    print(f"linha:{r};coluna:{t}")
