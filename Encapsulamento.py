class Pessoas:
    def __init__(self):
        self.Nome = ''
        self.Idade = 0
        self.Cpf = ''

    def set_Nome(self, Nome):
        self.Nome = Nome

    def set_Idade(self, Idade):
        if Idade > 0:
            self.Idade = Idade

    def set_Cpf(self, Cpf):
        self.Cpf = Cpf
        
Pessoas = Pessoas()
