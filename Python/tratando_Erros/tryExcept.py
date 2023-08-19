x = [1,2,3]
y = 2
z = 3
try:
    print(x+y)
    print(y+z)
    print("Funcionou!")
except Exception as error:
    print(f"Foi encontrado o erro {error}")