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

class Salário:
    def __init__(self, valor_da_hora, qtd_Horas, comissão) -> None:
        self.Valor_Hora = valor_da_hora
        self.Qtd_Hora = qtd_Horas
        self.Comissão = comissão

    def CalcularSalario(self):
        return (self.Valor_Hora * self.Qtd_Hora) + self.Comissão

class Funcionário:
    def __init__(self, nome, idade, valor_da_hora, qtd_hora, comissão) -> None:
        self.Nome = nome
        self.Idade = idade
        self.Salário = Salário(valor_da_hora, qtd_hora, comissão)

    def SalárioTotal(self):
        return self.Salário.CalcularSalario()

Funcionário = Funcionário('Calixto', 16, 22, 160, 1500)

print(f'Salário Total: {Funcionário.SalárioTotal()}')




