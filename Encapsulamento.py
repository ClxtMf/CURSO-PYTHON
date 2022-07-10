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

##########################################################################


class Estacionamento():
    def __init__(self, veiculo, placa, modelo, horarioEntrada, minutoEntrada, horarioSaida, minutoSaida):
        self.__veiculo = veiculo
        self.__placa = placa
        self.__modelo = modelo
        self.__horarioEntrada = horarioEntrada
        self.__minutoEntrada = minutoEntrada
        self.__horarioSaida = horarioSaida
        self.__minutoSaida = minutoSaida


    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        self.__veiculo = veiculo

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def horarioEntrada(self):
        return self.__horarioEntrada

    @horarioEntrada.setter
    def horarioEntrada(self, horarioEntrada):
        self.__horarioEntrada = horarioEntrada

    @property
    def minutoEntrada(self):
        return self.__minutoEntrada

    @minutoEntrada.setter
    def minutoEntrada(self, minutoEntrada):
        self.__minutoEntrada = minutoEntrada


    @property
    def horarioSaida(self):
        return self.__horarioSaida

    @horarioSaida.setter
    def horarioSaida(self, horarioSaida):
        self.__horarioSaida = horarioSaida

    @property
    def minutoSaida(self):
        return self.__minutoSaida

    @minutoSaida.setter
    def minutoSaida(self, minutoSaida):
        self.minutoSaida = minutoSaida



    def permanencia(self):
        if self.__horarioEntrada > self.__horarioSaida:
            hora_final = (self.__horarioSaida + 24) - self.__horarioEntrada
        else:
            hora_final = self.__horarioSaida - self.__horarioEntrada
            if self.__minutoEntrada > self.__minutoSaida:
                minuto_final = (self.__minutoSaida + 60) - self.__minutoEntrada
            else:
                minuto_final = self.__minutoSaida - self.__minutoEntrada
                print(f'A permanência foi de: {hora_final} horas e {minuto_final} minutos')

                tempo_minuto = hora_final * 60 + minuto_final
                if 1 >= tempo_minuto <= 60:
                    preco = 1
                    print(f'O valor a ser pago será de R$ {float(preco)}')
                elif 60 < tempo_minuto <= 120:
                    preco = 2
                    print(f'O valor a ser pago será de R$ {float(preco)}')
                elif 120 < tempo_minuto >= 180:
                    preco = 4.2
                    print(f'O valor a ser pago será de R$ {float(preco)}')
                elif 180 < tempo_minuto >= 240:
                    preco = 5.6
                    print(f'O valor a ser pago será de R$ {float(preco)}')
                elif tempo_minuto > 240:
                    preco = hora_final * 2
                    print(f'O valor a ser pago será de R$ {float(preco)}')
                else:
                    print('Tempo de permanência minima, não precisa pagar.')


veiculo = 'Carro'
placa = '2782-JDNX'
modelo = 'Gol'
horarioEntrada = 15
minutoEntrada = 20
horarioSaida = int(input('Horario de saida: '))
minutoSaida = int(input('Minuto de saida: '))

CARRO = Estacionamento(veiculo,placa,modelo,horarioEntrada,minutoEntrada, horarioSaida, minutoSaida)
CARRO.permanencia()
