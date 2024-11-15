from time import sleep

temp = int(input("diz tempo: "))


if temp > 0:
    while temp != 0:
        print(f"{temp}!")
        sleep(1)
        temp -= 1
    print("lançamento!")
else:
    print(">:(")
