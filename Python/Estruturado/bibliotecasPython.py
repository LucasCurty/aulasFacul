import math
import funcoes

a = eval(input('Entre com o coeficiente a da equação: '))
b = eval(input('Entre com o coeficiente b da equação: '))
c = eval(input('Entre com o coeficiente c da equação: '))


funcoes.calculaDelta(a, b, c)

print(f'O valor calculado de delta foi {delta}')

# delta > 0 : equação tem 2 reízes reais
# delta = 0 : equação tem 1 raíz real
# delta < 0 > equação não tem raiz real

if delta > 0:
  print("A equação tem 2 raízes reais.")
  raiz1 = (-b + math.sqrt(delta))/2*a
  raiz2 = (-b - math.sqrt(delta))/2*a
  print(f'As raízes da equação são {raiz1} e {raiz2}')
elif delta ==0:
  print("A equação tem 1 raíz real")
  raiz = (-b + math.sqrt(delta))/2*a
  print(f'As raízes da equação é {raiz}')
else: print("A equação não tem raiz real")