x = int(input("Diz-me um nº inteiro  "))
h = x
m = 0
while round(x) != 1:
    print(f"{round(x)}")
    f = x
    x = f / 2
    n = m
    m = n + 1
    round(x)
    if x == 0.0:
        break
print("1")
f = h
if f == 2:
    print(f"O número {h} é primo")
elif f == 1:
    print(f"O número {h} não é primo")
else:
    for i in range(2,f):
       if (f%i) == 0:
          print(f"O número {h} não é primo")
          u = True
       else:
          print(f"O número {h} é primo")
          u = False
       if u == True:
           break
n = m
m = n
print(f"foi divisivel {m} vezes")
