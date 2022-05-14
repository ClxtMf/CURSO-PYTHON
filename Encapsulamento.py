class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__cpf = ''

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_cpf(self):
        return self.cpf


pessoa = Pessoa()

"""""""""""""""""""""""""""""""""""""""""""""

upgrade 2.0

class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__cpf = ''
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


pessoa = Pessoa()


pessoa.nome = input('Digite o seu nome: ')
pessoa.idade = int(input('Digite a sua idade: '))
pessoa.cpf = input('Digite o seu cpf: ')

print(f'Nome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'CPF: {pessoa.cpf}')
