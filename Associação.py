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

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Salario:
    def __init__(self, valor_da_hora, qtd_Horas, comissao) -> None:
        self.Valor_Hora = valor_da_hora
        self.Qtd_Hora = qtd_Horas
        self.Comissao = comissão

    def CalcularSalario(self):
        return (self.Valor_Hora * self.Qtd_Hora) + self.Comissão

class Funcionario:
    def __init__(self, nome, idade, valor_da_hora, qtd_hora, comissao) -> None:
        self.Nome = nome
        self.Idade = idade
        self.Salário = Salário(valor_da_hora, qtd_hora, comissao)

    def SalárioTotal(self):
        return self.Salário.CalcularSalario()

Funcionario = Funcionario('Calixto', 16, 22, 160, 1500)

print(f'Salário Total: {Funcionario.SalárioTotal()}')


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
