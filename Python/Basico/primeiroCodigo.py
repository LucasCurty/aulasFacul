print("Hello World!")

# Comentario de uma linha.

""" 
    Comentario de varias linhas.
"""
def mult(numb):
    global a     # Todas as referências á variável a são para o global
    a = 2        # variavel de escopo local, sera alterado
    print(f"Dentro da função, a variável (a) vale: {a}")
    return a * numb

a = 3 # Variável de escopo global
b = mult(5)
print(f"Agora o resultado da multiplicação: {b}")
print(f"Fora da função, a variável (a) vale: {a}")