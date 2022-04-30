"""
A programação Orientada a Objeto(POO)
"""

class Pessoa:

    # Método (função) construtor. sempre será chamado quando um novo objeto é criado

    def __init__(self): # self = fco

        # Atributos do objeto, sempre defidos através da palavra 'self' + . + o nome do atributo
        self.nome = input('Informe o nome: ')
        self.sexo = input('Informe o sexo M - F: ')
        self.cpf = int(input('Informe o cpf: '))

Fco = Pessoa()
print(Fco.cpf)

""""""""""""""""""""""""""""""""""""""""""""

class ContaBancária:
    def __init__(self, titular, númerodaconta, saldo, vip):
        self.titular = titular
        self.númerodaconta = númerodaconta
        self.Saldo = saldo
        self.vip = vip
Calixto = ContaBancária('Calixto', 202020.5, 2.000, 'Sim')
print(Calixto.númerodaconta)


Upgrad-0.1

titular = input('Informe o nome do titular: ')
númeroDaConta = float(input('informe o número da conta: '))
saldo = float(input('informe o saldo do titular: '))
vip =  bool(input('Informe se você é vip S - N: '))

class ContaBancária:
    def __init__(self):
        self.titular = titular
        self.númerodaconta = númeroDaConta
        self.Saldo = saldo
        self.vip = vip
        
        if vip == True:
            print(input('Deseja ver seus beneficios S - N ? '))
        else:
            print(input('Deseja se fazer o cadastro vip S - N ?'))
Calixto = ContaBancária()

"""""""""""""""""""""""""""""""""""""""""""""""""

Upgrade - 0.2

class ContaBancaria:

    def __init__(self, titular, numeroDaConta, saldo, vip):
        self.titular = titular
        self.numeroDaConta = numeroDaConta
        self.saldo = saldo
        self.vip = vip


    def sacar(self, valor):
        if valor > self.saldo:
            print('Seu saldo insuficiente')
        else:
            self.saldo -= valor

    def depositar(self, valor):
        if valor >= 0:
            self.saldo = self.saldo + valor
        else:
            print('Valor inválido')




titular = input('Informe o titular da conta: ')
numeroDaConta = int(input('Informe o número da conta: '))
saldo = float(input('Informe o seu saldo: '))
vip = bool(input('Informe o VIP: '))

conta1 = ContaBancaria(titular, numeroDaConta, saldo, vip)

print(f'Seu saldo antigo: {conta1.saldo}')


conta1.saldo = 3000.50

print(f'Seu saldo novo: {conta1.saldo}')


conta1.sacar(2000)

print(f'Seu saldo após o saque: {conta1.saldo}')


conta1.depositar(1500)

print(f'Seu saldo após o deposito: {conta1.saldo}')

