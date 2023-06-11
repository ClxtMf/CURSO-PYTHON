class BichinhoVirtual:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade
        self.Saude = 100
        self.Fome = 100

    @property
    def Nome(self):
        return self.__Nome

    @Nome.setter
    def Nome(self, Nome):
         self.__Nome = Nome

    @property
    def Idade(self):
        return self.__Idade

    @Idade.setter
    def Idade(self, Idade):
        self.__Idade = Idade

    @property
    def Saude(self):
        return self.__Saude

    @Saude.setter
    def Saude(self, Saude):
        self.__Saude = Saude

    @property
    def Fome(self):
        return self.__Fome

    @Fome.setter
    def Fome(self, Fome):
        self.__Fome = Fome

    def get_Humor(self):
        if self.__Fome >= 60 and self.__Saude >= 75:
            print('Estou muitooooo bemmm!!!')
        elif self.__Fome >= 45 and self.__Saude >= 55:
            print('Preciso de cuidados, pfvr.')
        elif self.__Fome >= 30 and self.__Saude >= 40:
            print('Estou a passar muito mal, me ajude.')
        else:
            print('Estou morrendo!!!')

Claudinho = BichinhoVirtual('Claudinho', 10)
Claudinho.Fome = 50
Claudinho.Saude = 50

Claudinho.get_Humor()

######################################################################

class Salario:
    def __init__(self, valor_da_hora, qtd_Horas, comissao) -> None:
        self.Valor_Hora = valor_da_hora
        self.Qtd_Hora = qtd_Horas
        self.Comissao = comissao

    def CalcularSalario(self):
        return (self.Valor_Hora * self.Qtd_Hora) + self.Comissão

class Funcionario:
    def __init__(self, nome, idade, valor_da_hora, qtd_hora, comissao) -> None:
        self.Nome = nome
        self.Idade = idade
        self.Salario = Salario(valor_da_hora, qtd_hora, comissao)

    def SalarioTotal(self):
        return self.Salario.CalcularSalario()

Funcionario = Funcionario('Calixto', 16, 22, 160, 1500)

print(f'Salario Total: {Funcionario.SalarioTotal()}')


######################################################################


class Endereco:
    def __init__(self, rua, bairro, cidade):
        self.__rua = rua
        self.__cidade = cidade
        self.__bairro = bairro


    @property
    def rua(self):
        return self.__rua

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade


class Empresa:
    def __init__(self, nome, area):
        self.__nome = nome
        self.__area = area
        self.__enderecos = []


    @property
    def nome(self):
        return self.__nome

    @property
    def area(self):
        return self.__area


    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @area.setter
    def nome(self, area):
        self.__area = area

    def inserirEndereco(self, rua, bairro, cidade):
        self.obj_endereco = Endereco(rua, bairro, cidade)
        self.__enderecos.append(self.obj_endereco)
        print(f'Endereço cadastrado com sucesso!!')

    def exibirEnderecos(self):
        for endereco in self.__enderecos:
            print(f'Rua: {endereco.rua} - Bairro: {endereco.bairro} - Cidade: {endereco.cidade}')



pizza_hut = Empresa('Pizza Hut', 'Alimentício')
pizza_hut.inserirEndereco('Av Santos Dummont', 'Aldeota', 'Fortaleza')
pizza_hut.inserirEndereco('Pe. Antonio Thomaz', 'Água Fria', 'Fortaleza')
pizza_hut.exibirEnderecos()

######################################################################

class Produto:
    def __init__(self, codigo, nome, valor):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor

class Carrinho:
    def __init__(self):
        self.produtos = []

    def addCarrinho(self, produto):
        self.produtos.append(produto)

        
    def listarProdutos(self):
        for produto in self.produtos:
            print(f'Código: {produto.codigo}')
            print(f'Nome do Produto: {produto.nome}')
            print(f'Preço: {produto.valor}')

    def calcularTotal(self):
        total = 0
        for produto in self.produtos:
            total = total + produto.valor

        print(f'Valor total da sua compra: {total}')


carrinho = Carrinho()
while True:
    print('-- SELECIONE UMA OPÇÃO --')
    print('1 - Adicionar produto ')
    print('2 - Listar Produtos ')
    print('3 - Finalizar compra ')
    print('4 - Sair ')

    opcao = int(input('Selecione entre 1 - 4: '))

    if opcao == 4:
        break

    if opcao == 1:
        codigo = int(input('Informe o código do produto: '))
        nome = input('Informe o nome do produto: ')
        valor = float(input('Informe o valor do produto: '))

        produto = Produto(codigo, nome, valor)
        carrinho.addCarrinho(produto)

    if opcao == 2:
        carrinho.listarProdutos()

    if opcao == 3:
        carrinho.calcularTotal()
        
        
        
######################################################################


class Escola:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = ['Dev FullStack', 'Fotografia', 'Design']
        self.alunos = []

    def listarAlunos(self):
        for aluno in self.alunos:
            print(f'Matricula: {aluno.matricula}')
            print(f'Nome: {aluno.nome}')
            print(f'Idade: {aluno.idade}')
            print(f'Curso: {aluno.curso}')
            print(f'-----------------------------\n')

    def matricularAluno(self, aluno):
        self.alunos.append(aluno)

class Aluno:
    def __init__(self, matricula, nome, idade, curso):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso



aluno1 = Aluno(1, 'João', 19, 'Dev FullStack')
aluno2 = Aluno(2, 'Maria', 21, 'Fotografia')


escola = Escola('Infinity School', 'Santos Dummont')
escola.matricularAluno(aluno1)
escola.matricularAluno(aluno2)

escola.listarAlunos()


######################################################################


'''
class Pessoa:
    def __init__(self, Nome, Idade, Cpf) -> None:
        self.Nome = Nome
        self.Idade = Idade
        self.Cpf = Cpf
        

class Aluno(Pessoa):
    pass


class Professor(Pessoa):
    pass


class Coordenador(Pessoa):
    pass


a1 = Aluno('Calixto', 16, '822.355.533-35')
print(f'Nome: {a1.Nome}')
print(f'Idade: {a1.Idade}')
print(f'Cpf: {a1.Cpf}')
'''

class Funcionario:
     def __init__(self):
         self.__matricula = ''
         self.__nome = ''
         self.__salario = 0

     @property
     def matricula(self):
         return self.__matricula

     @property
     def nome(self):
         return self.__nome

     @property
     def salario(self):
         return self.__salario

     @matricula.setter
     def matricula(self, matricula):
         self.__matricula = matricula

     @nome.setter
     def nome(self, nome):
         self.__nome = nome

     @salario.setter
     def salario(self, salario):
         self.__salario = salario

class Estagiario(Funcionario):
     ...
     
class Gerente(Funcionario):
     ...

estagiario = Estagiario()
estagiario.matricula = '3423423'
estagiario.nome = 'Rodrigo'
estagiario.salario = 10000
print(estagiario.matricula)
print(estagiario.nome)
print(estagiario.salario)

class Funcionario:
     def __init__(self, matricula, nome, salario):
         self.matricula = matricula
         self.nome = nome
         self.salario = salario
 
class Estagiario(Funcionario):
     ...

class Gerente(Funcionario):
     ...

estagiario = Estagiario(342342, 'Lucas', 10000)
gerente = Gerente(546455, 'Rodrigo', 60000)

######################################################################


class Funcionario:
     def __init__(self, matricula, nome, salario):
         self.matricula = matricula
         self.nome = nome
         self.salario = salario
 
class Gerente(Funcionario):
     def __init__(self, matricula, nome, salario, Setor, Comissao):
         super().__init__(matricula, nome, salario)
         self.Setor = Setor
         self.Comissao = Comissao

     def Contratar(self, qtd_funcionarios):
        if qtd_funcionarios < 10:
          print(f'Contratar: {10 - qtd_funcionarios}')
        else:
            print('Temos gente o suficiente')
       

class Estagiario(Funcionario):
     def __init__(self, matricula, nome, salario, qtd_Horas):
         super().__init__(matricula, nome, salario)
         self.qtd_Horas = qtd_Horas

     def contratacao(self):
        if self.qtd_Horas >= 300:
            print('Contratato!!!')
        else:
            print('Ainda não acabou.')



estagiario = Estagiario('01', 'marcio', '2.000', 300)
estagiario.contratacao()
print(f'Matricula: {estagiario.matricula}')
print(f'Nome: {estagiario.nome}')
print(f'Sálario: {estagiario.salario}')
print(f'Quantidade Horas: {estagiario.qtd_Horas}')
estagiario.contratacao

print('--------------------------------------------\n')

gerente = Gerente('02', 'joao', '3.000', 'gerencia', '2.000')
gerente.Contratar(5)
print(f'Matricula: {gerente.matricula}')
print(f'Nome: {gerente.nome}')
print(f'Sálario: {gerente.salario}')
print(f'Setor: {gerente.Setor}')
print(f'Comissão: {gerente.Comissao}')

######################################################################

class Conta:
    def __init__(self, Numero, Titular, Saldo) -> None:
        self.__Numero = Numero
        self.__Titular = Titular
        self.__Saldo = Saldo
    
    @property
    def Numero(self):
        return self.__Numero
    @Numero.setter
    def Numero(self, Numero):
        self.__Numero = Numero

    @property
    def Titular(self):
        return self.__Titular
    @Titular.setter
    def Titular(self, Titular):
        self.__Titular = Titular
        
    @property
    def Saldo(self):
        return self.__Saldo
    @Saldo.setter
    def Saldo(self, Saldo):
        self.__Saldo = Saldo


    def sacar(self, Valor):
        if self.Saldo - Valor > 0:
            self.Saldo -= Valor
            print('Saque realizado.')
    
    def depositar(self, Valor):
        if Valor > 0:
            self.Saldo += Valor
            print('Deposito feito.')

class ContaCorrente(Conta):
    def __init__(self, Numero, Titular, Saldo, Limite) -> None:
        super().__init__(Numero, Titular, Saldo)
        self.__Limite = Limite

    @property
    def Limite(self):
        return self.__Limite
    @Limite.setter
    def Limite(self, Limite):
        self.__Limite = Limite   

    def extrato(self):
        print(f'Número da conta: {self.__Numero}')
        print(f'Número da conta: {self.__Titular}')
        print(f'Número da conta: {self.__Saldo}')
        print(f'Número da conta: {self.__Limite}')

class Poupanca(Conta):
    def __init__(self, Numero, Titular, Saldo, rendimento) -> None:
        super().__init__(Numero, Titular, Saldo)
        self.rendimento = rendimento

    def RendimentoMensal(self):
        self.__Saldo = self.__Saldo + (self.__Saldo * (self.rendimento / 100))
        print(f'Saldo após o rendimento: {self.__Saldo}')


Conta01 = Conta('020202-2', 'Calixto', '6.000,00')
print(f'Número da conta: {Conta01.Numero}')
print(f'Nome do titular: {Conta01.Titular}')
print(f'Saldo do titular: {Conta01.Saldo}')
