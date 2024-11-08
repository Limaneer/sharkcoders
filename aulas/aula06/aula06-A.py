x = float(input("qual o salário atual?   "))
if x < 0:
    t = x
    x = t * -1
    print(":| a sério?")
if x < 500:
    n = x * 1.15
    m = "15%"
elif x >= 500 and x <= 1000:
    n = x * 1.10
    m = "10%"
elif x > 1000:
    n = x * 1.05
    m = "5%"
print(f"o reajuste será de {m} e o salário novo é {n:.2f} euros")
