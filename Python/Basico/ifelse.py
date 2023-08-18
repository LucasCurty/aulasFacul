temp = int(input("Qual a temperatura atual?"))

if temp >= 30:
    print("Está quente")
elif temp <= 0:
    print("Esta bem frio")
    if temp < -50:
        print("Congelou foi tudo!")


