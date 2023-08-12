variavel_numero = 1
variavel_string = 'testo numero 1'
variavel_boolean = True
variavel_vetor = [1, 'dois', True]

print("variaveis tipos")

print(type(variavel_numero))
print(type(variavel_string))
print(type(variavel_boolean))
print(type(variavel_vetor[0]),
    type(variavel_vetor[1]),
    type(variavel_vetor[2]))

print('----------------------------------------------------------------')
print('metodos strings')
#Trabalhando com strings

hello = "Hello"
print(hello.lower()) #transforma o texto em low case
print(hello.upper()) #transforma o texto em upper case
print(hello.split()) #Devoler uma lista ou quebra em lista uma string

print('----------------------------------------------------------------')
print('Listas')

my_list = [1,2,3]
print(type(my_list))
print(my_list[1])
print(my_list[-1])
print(my_list[:])

print('----------------------------------------------------------------')

print("Métodos básicos de listas")
my_list.append("4") #adiciona ao final da lista
print(my_list)
print(my_list.pop()) #remove o ultimo item da lista/ coloquei o print pra mostrar que ele retorna o item removido
my_list.sort() #arruma a lista sequenciamente
my_list.reverse()#inverte a lista decrescente
print(my_list)

print('----------------------------------------------------------------')
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista4 = [lista1,lista2,lista3]

print(lista4[0][0])
print('----------------------------------------------------------------')
print("dicionários ")
#Dictopnários ou o indicador precisa ser int, string ou float; n
#string
meu_dicionario = {
    "nome" : "Lucas",
    "idade": 27,
    "ende" : ['rua', 'cidade']
}
#Para acessar esses dados precisamos passar o indicador
print(meu_dicionario["nome"])
print(meu_dicionario["idade"])
print(meu_dicionario["ende"][0])
print(meu_dicionario["ende"][1])
#tbm podemos adicionar ou alterar
meu_dicionario["nome"] = "Joao" #alterando
meu_dicionario["Time"] = "Fluminense" #adicionando
print(meu_dicionario) 
meu_dicionario["Time"] = {"principal": "Fluminense", "secundario":"Real Madrid"} #aletando e adicionando
print(meu_dicionario) 
##--------------------------------------
print('----------------------------------------------------------------')
print('Metodos do dicionarios')

print(meu_dicionario.keys()) #retorna o indicador
print(meu_dicionario.items())#retorna todos os itens
print(meu_dicionario.values())#retorna somente os valores dentro dos indicadores
print('----------------------------------------------------------------')

print('Tuplas')
#Tuplas são a mesma coisa que arrays, porem a diferença é que nao sao alteraveis.abs
lista_tupla = (1,2,3) # sim, tuplas definimos com ( ) parenteses
print(lista_tupla[:])
#tbm pode ser usada para criar e definir mais de uma variavel por exemplo:
a,b = (2,4)
print(a)
print(b)
print('----------------------------------------------------------------')

print('Input, Sets, Booleanos')
#inputs
#nome = input("Qual seu nome? ")
#print(f'seu nome é {nome}')
#set
x = set()
print(x)
x.add(1)
x.add(2)
x.add("Lucas")
print(x)
x.add(2)
print(x)
x.add(0)
print(x)
y = [1,2,3,6]
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print('----------------------------------------------------------------')

print('Boolean')
verdadeiro = True
falso = False
print(verdadeiro, falso)



