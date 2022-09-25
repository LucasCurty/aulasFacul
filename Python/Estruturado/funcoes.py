def calculaDelta(coef1, coef2, coef3):
  # delta da eg 2° grau = b² - 4.a.c
   global delta 
   delta = coef2*coef2 - 4*coef1*coef3


a = eval(input('Entre com o coeficiente a da equação: '))
b = eval(input('Entre com o coeficiente b da equação: '))
c = eval(input('Entre com o coeficiente c da equação: '))


calculaDelta(a, b, c)

print(f'O valor calculado de delta foi {delta}')

# delta > 0 : equação tem 2 reízes reais
# delta = 0 : equação tem 1 raíz real
# delta < 0 > equação não tem raiz real

if delta > 0:
  print("A equação tem 2 raízes reais.")
elif delta ==0:
  print("A equação tem 1 raíz real")
else: print("A equação não tem raiz real")