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
