class Veiculo:
    def __init__(self, marca, modelo, velocidadeMax, capacidade, tanque):
        self.marca = marca
        self.modelo = modelo
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = 0
        self.ligado = False
        self.capacidade = capacidade
        self.tanque = tanque

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O Veiculo foi ligado...')
        else:
            print('O Veiculo já está ligado...')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O Veiculo foi desligado...')
        else:
            print('O Veiculo já está desligado...')

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidadeAtual += velocidade
            print(f'Acelerando.. Velocidade atual: {self.velocidadeAtual}')
        else:
            print('O Veiculo está desligado...')

    def frear(self, freio):
        if self.ligado:
            self.velocidadeAtual -= (self.velocidadeAtual * freio / 100)
            print(f'Freando... Velocidade atual: {self.velocidadeAtual}')
        else:
            print('O Veiculo está desligado...')

class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidadeMax, capacidade, tanque, abs, qtd_portas):
        super().__init__(marca, modelo, velocidadeMax, capacidade, tanque)
        self.abs = abs
        self.qtd_portas = qtd_portas

    def re(self, velocidade):
        if self.ligado:
            if velocidade < 60:
                self.velocidadeAtual = 0
                self.velocidadeAtual -= velocidade
                print(f'Dando ré... Velocidade atual: {self.velocidadeAtual}')
            else:
                print('Velocidade não pode ser inferior a -60km/h')
        else:
            print('O carro está desligado...')

class Moto(Veiculo):
    def __init__(self, marca, modelo, velocidadeMax, capacidade, tanque, cilindradas):
        super().__init__(marca, modelo, velocidadeMax, capacidade, tanque)
        self.cilindradas = cilindradas

print('---------------CARRO------------------')
gol = Carro('Volks', 'Gol 1.4', 160, 5, 20, True, 4)
gol.ligar()
gol.acelerar(100)
gol.frear(50)
gol.re(45)
gol.desligar()

print('---------------------------------------------\n\n')
print('--------------MOTO-------------------')

tenere = Moto('Yamaha', 'Teneré', 130, 2, 15, 250)
tenere.ligar()
tenere.acelerar(80)
tenere.frear(20)
tenere.desligar()



######################################################################

class Pessoa:
    def __init__(self, estado, renda):
        self.estado = estado
        self.renda = renda
        self.imposto = 0

    def calcularImposto(self):
        ...

    def exibirDados(self):
        print(f'Estado: {self.estado}')
        print(f'Renda: {self.renda}')
        print(f'Imposto: {self.imposto}')
        print(f'-------------------------\n\n')

class Fisica(Pessoa):
    def __init__(self, estado, renda, nome, cpf, dt_nascimento):
        super().__init__(estado, renda)
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento

    def calcularImposto(self):
        if self.renda > 2000:
            self.imposto = self.renda * 0.05
            print(f'Imposto a pagar: {self.imposto}')
        else:
            print('Você não precisa pagar imposto!!')

    def exibirDados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Dt de Nascimento: {self.dt_nascimento}')
        super().exibirDados()

class Juridica(Pessoa):
    def __init__(self, estado, renda, cnpj, nf,rs):
        super().__init__(estado, renda)
        self.cnpj = cnpj
        self.rs = rs
        self.nf = nf

    def calcularImposto(self):
        self.imposto = self.renda * 0.2
        print(f'Imposto a pagar: {self.imposto}')

    def exibirDados(self):
        print(f'Nome Fantasia: {self.nf}')
        print(f'Razão Social: {self.rs}')
        print(f'CNPJ: {self.cnpj}')
        super().exibirDados()



maria = Fisica('CE', 3000, 'Maria', '012.321.456-65', '15/05/2000')
infinity = Juridica('BA', 200000, '01.123.654/0001-32','Infinity School', 'Infinity Treinamentos')

maria.calcularImposto()
infinity.calcularImposto()


maria.exibirDados()
infinity.exibirDados()

from abc import ABC, abstractmethod

class Ave(ABC):
    def __init__(self, corPenas, voar):
        self.corPenas = corPenas
        self.voar = voar

    @abstractmethod
    def cantar(self):
        print('Estou cantando...')

class BemTiVi(Ave):
    def cantar(self):
        super().cantar()
        print('BEM-TI-VI')


class PicaPau(Ave):
    def cantar(self):
        print('HEHEHEHE HE HEHEHEHE HE!!!!!')
        print('HMMM BOLO DE MURANGO')

class Galinha(Ave):
    def cantar(self):
        print('CÓ-CÓ-CÓ!!')


bentivi = BemTiVi('Amarelo', True)
picapau = PicaPau('Azul', True)
galinha = Galinha('Preta', False)


bentivi.cantar()
picapau.cantar()
galinha.cantar()









 
