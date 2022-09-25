for item in range(2,9,3):
    print(item)

# for com string
nome = input("Entre com seu nome: ")
for letra in nome:
    print(letra)
    
# for com array
amigos = ['Laura', 'Jose', 'João', 'Maria']
for pessoa in amigos:
    print(pessoa)
    
#While
palavra = input('Entre com uma palavra: ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: ')
print('Você conseguiu sair.')