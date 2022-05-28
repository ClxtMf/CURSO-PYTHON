from abc import ABC, abstractmethod

class App:
    def __init__(self, Nome, ConsumoDeBateria, ConsumoDeMemoria) -> None:
        self.Nome = Nome
        self.ConsumoDeBateria = ConsumoDeBateria
        self.ConsumoDeMemoria = ConsumoDeMemoria
           
class SmartPhone(ABC):

    @abstractmethod
    def __init__(self, Fabricante, Memoria) -> None:
        self.Fabricante = Fabricante
        self. Memoria = Memoria
        self. Bateria = 100
        self.ConsumoMemoria = 0
        self.Ligado = False
        self.apps = []

    @abstractmethod
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O smartphone está ligado...')
        else:
            print('Já está ligado...')
            
    @abstractmethod
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O smartphone foi desligado...')
        else:
            print('já está desligado...')

    @abstractmethod
    def AbrirApp(self, Nome, ConsumoBateria, ConsumoMemoria):
        pass

    @abstractmethod
    def FecharApp(self, Nome):
        pass


    def ListarApps(self):
        apps = 0
        for i in range(apps):
            apps += 1
