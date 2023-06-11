from abc import ABC, abstractmethod

class App:
    def __init__(self, Nome, ConsumoDeBateria, ConsumoDeMemoria) -> None:
        self.Nome = Nome
        self.ConsumoDeBateria = ConsumoDeBateria
        self.ConsumoDeMemoria = ConsumoDeMemoria
           
class SmartPhone(ABC):
    def __init__(self, Fabricante, Memoria) -> None:
        self.Fabricante = Fabricante
        self. Memoria = Memoria
        self. Bateria = 100
        self.ConsumoMemoria = 0
        self.Ligado = False
        self.apps = []

    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print('Já está ligado...')
            
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print('já está desligado...')


    @abstractmethod
    def AbrirApp(self, Nome, ConsumoBateria, ConsumoMemoria):
        pass
    
    @abstractmethod
    def FecharApp(self, Nome):
        pass
    
    @abstractmethod
    def ListarApps(self):
        for app in self.apps:
            print(f'Nome: {app.nome}')
            print(f'Bateria: {app.ConsumoDeBateria}')
            print(f'Mémoria: {app.ConsumoDeMemoria}')
            print('--------------------------------')

    def ExibirDados(self):
        print(f'O fabricante: {self.Fabricante}')
        


class Xiaomi(SmartPhone):
    def AbrirApp(self, Nome, ConsumoBateria, ConsumoMemoria):
        if self.ligado:
            app = App(Nome, ConsumoBateria, ConsumoMemoria)
            if self.Bateria - app.ConsumoDeBateria <= 0:
                print('Bateria descarregou...')
                self.desligar()
                if self.ConsumoMemoria + app.ConsumoDeMemoria > self.Memoria:
                    print('Mémoria estourou...')
                    self.desligar()
                else:
                    self.append(app)
                    

    def FecharApp(self, Nome):
        return super().FecharApp(Nome)

    def ListarApps(self):
        return super().ListarApps()


class Iphone(SmartPhone):
    def __init__(self, Fabricante, Memoria) -> None:
        super().__init__(Fabricante, Memoria)
        self.Fabricante = Fabricante
        self.Memoria = Memoria

    def AbrirApp(self, Nome, ConsumoBateria, ConsumoMemoria):
        return super().AbrirApp(Nome, ConsumoBateria, ConsumoMemoria)

    def FecharApp(self, Nome):
        return super().FecharApp(Nome)

    def ListarApps(self):
        return super().ListarApps()