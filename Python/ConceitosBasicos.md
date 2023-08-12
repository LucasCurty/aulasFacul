### Operadores
```
( + ) Adição 
( - ) Subtração
( * ) Multiplicação
( / ) Divisão
( ** ) Exponenciação
```
Operadores aritiméticos só funcionam em numeros.

---
### Operadores realacionais
```
( = ) Igual à
(< >) Diferente de outros porem dizer (!)
( > ) Maior que
( < ) Menor que
(> =) Maior ou  Igual 
(< =) Menor ou Igual 
```
 Retorna sim ou não, True o False

---
### Estrutura de controle de fluxo
```python
condicional = True #Variavel condicional para controle de fluxo

def fazer(x, y):   #Função com parametros de controle
    if condicional: #Condinional, Se condicional printe x
        print(x)
    else:           #Condicional, Se não, printe y
        print(y)
```
ou
```python
condicional = True #Variavel condicional para controle de fluxo

def fazer():   #Função com parametros de controle
    if condicional: #Condinional, Se condicional printe x
        print(x)
```
Também podemos apenas passar o "se" sem o "se nao"

---
### Estrutura de repetição
```python
condicional = True

while condicional:
    print(f'A condição {condicional}')
    condicional = False
    print(f'A condição é {condicional}')
 ```