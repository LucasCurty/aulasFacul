class Conta:
  def __init__(self, numero, cpf, nomeTitular, saldo):
    self.numero = numero
    self.cpf = cpf
    self.nomeTitular = nomeTitular
    self.saldo = saldo

  def depositar(self, valor):
    self.saldo += valor
    print(f'Valor depositado com sucesso')
  def sacar(self, valor):
    if self.saldo < valor:
      print(f'Seu saldo é de {self.saldo}$, não foi possivel sacar.')
    else:
      self.saldo -= valor
      