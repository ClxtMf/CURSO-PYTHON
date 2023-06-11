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

class ContaBancaria:
    def __init__(self, titular, numerodaconta, saldo, vip):
        self.titular = titular
        self.numerodaconta = numerodaconta
        self.Saldo = saldo
        self.vip = vip
Calixto = ContaBancaria('Calixto', 202020.5, 2.000, 'Sim')
print(Calixto.numerodaconta)


# Upgrad-0.1

titular = input('Informe o nome do titular: ')
numeroDaConta = float(input('informe o número da conta: '))
saldo = float(input('informe o saldo do titular: '))
vip =  bool(input('Informe se você é vip S - N: '))

class ContaBancaria:
    def __init__(self):
        self.titular = titular
        self.numerodaconta = numeroDaConta
        self.Saldo = saldo
        self.vip = vip
        
        if vip == True:
            print(input('Deseja ver seus beneficios S - N ? '))
        else:
            print(input('Deseja se fazer o cadastro vip S - N ?'))
Calixto = ContaBancaria()

#############################################################################

# Upgrade - 0.2

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

#############################################################################

class Elevador:
    def __init__(self, capacidade, qtd_andares, qtd_pessoas, andar_atual):
        self.capacidade = capacidade
        self.qtd_andares = qtd_andares
        self.qtd_pessoas = qtd_pessoas
        self.andar_atual = andar_atual

    def subir(self):
        if self.andar_atual < self.qtd_andares - 1:
            self.andar_atual += 1
            print('Subindo...')
            print(f'Andar atual: {self.andar_atual}')
        else:
            print('Você já está no ultimo andar!')

    def descer(self):
        if self.andar_atual == 0:
            print('Você já esta no terreo!!')
        else:
            self.andar_atual -= 1
            print('Descendo...')
            print(f'Andar atual: {self.andar_atual}')

    def entrar(self, qtd_pessoas):
        if self.qtd_pessoas + qtd_pessoas >= self.capacidade:
            print('Elevador lotado!!!')
        else:
            self.qtd_pessoas += qtd_pessoas
            print('Entrando...')
            print(f'Quantidade de pessoas: {self.qtd_pessoas}')

    def sair(self, qtd_pessoas):
        if self.qtd_pessoas - qtd_pessoas < 0:
            print('Não tem essa quantidade dentro do elevador!!')
        else:
            self.qtd_pessoas -= qtd_pessoas
            print('Saindo...')
            print(f'Quantidade de pessoas: {self.qtd_pessoas}')




elevador = Elevador(20,15,7,5)

plaza = Elevador(30, 10, 9, 9)

elevador.subir()
elevador.subir()
elevador.subir()
elevador.entrar(5)
elevador.sair(7)
elevador.descer()
elevador.descer()
