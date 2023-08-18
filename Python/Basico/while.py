#While significa enquanto, ou seja. Enquanto a condição for verdadeira, ela vai executar o loop.

#while booleano:(VERDADEIRO)
#    codigo
x = 0
while x < 10:
    print(f"Ainda rodando! {x +1}")
    x += 1
#IMPORTANTE: Depois que a condição se tornar falsa, ele executa  o else.. ou seja!
else:
    print(f"Fim de contagem, o x é igual a {x}")

print("--------------------------------------------------------------------------------------------------")
#Algumas palavras chaves
#CONTINUE serve para pular o codigo a ser executado abaixo e voltar a repetição. por exemplo:
x = 0
while x < 10:
    print(f"um print com continue")
    x += 1
    if x == 5: #se eu tirar e identar ele nao executa nenhuma vez o codigo abaixo
        continue  #melhorando
    print(f"Não vai ser executado esse print no {x} 5")
else:
    print(f"Fim de contagem, o x é igual a {x}")

#BREACK serve para parar o laço.
print("--------------------------------------------------------------------------------------------------")
x = 0
while x < 10:
    print(f"printando ate o break {x + 1} vezes")
    x += 1
    if x == 5: #se eu tirar e identar ele nao executa nenhuma vez o codigo abaixo
        break 
print(f"esse codigo vai rodar ate o 5")
print(x)