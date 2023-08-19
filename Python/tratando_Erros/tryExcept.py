x = [1,2,3]
y = 2
z = 3
try: #Tente executar
    print(x+y)
    print(y+z)
    print("Funcionou!")
except Exception as error: #Se algum erro acima, execute:
    print(f"Foi encontrado o erro {error}")
