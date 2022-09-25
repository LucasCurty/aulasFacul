soma_pares = 0
total_pares = 0

#range tras numeros inteiros de acordo com o colocado nos parametros começando pelo primeiro parametro ate o segundo parametro sendo esse ignorado, o terceiro parametro diz a quantidade da contagem, se fosse 2 ele iria contar de 2 em 2.
for numero in range(1,11,1): 
    if numero%2 == 0:
        soma_pares += numero
        total_pares += 1
    else:
        continue
print(f'O total de numeros pares foi {soma_pares} e o total de pares foi {total_pares}')
print(f'A meidia é {soma_pares/total_pares}')