n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))

fake = False

if n1 > 100 or n2 > 100 or n1 < 0 or n2 < 0:
    fake = True
    print("mentir é feio")


nfinal = ((n1 + n2)/2) // 1 + 1

if fake == False:
    if nfinal >= 60:
         print(f"parabéns! passaste com uma nota de {nfinal}")
    else:
         print(f"falhaste com uma nota de {nfinal}")



