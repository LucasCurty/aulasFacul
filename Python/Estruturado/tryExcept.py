"""
try:
  num = eval(input('Insira um número inteiro: '))
  print(f'seu número é o {num}')
except:
  print("Enre com o valor numérico e não letras")
"""
numerador = eval(input('Entre com numero da fração: '))
denominador = input('Entre com o denominador da fração: ')

try:
  print(f'A divisão vale {numerador/denominador}')
except ZeroDivisionError:
  print("Os parâmetros informados são inválidos - Divisão por zero")
except:
  print("Não foi possivel executar a operação")