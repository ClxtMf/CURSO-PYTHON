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
