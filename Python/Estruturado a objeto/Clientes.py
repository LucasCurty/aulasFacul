import Conta 

cliente1 = Conta.Conta(0, 123456, "Arnaldo", 1500)
cliente2 = Conta.Conta(1, 654321, "Bete", 2000)

cliente1.sacar(2000)
print(f'Essa é a conta do {cliente1.nomeTitular}, e ele tem {cliente1.saldo} Reais na conta.\n')

cliente2.depositar(300) 
print(f'Essa é a conta do {cliente2.nomeTitular}, e ele tem {cliente2.saldo} Reais na conta.')