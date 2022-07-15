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

##########################################################################
-WorkShop...
    
### Questão 01
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O {n1} é maior')
elif n2 > n1:
 print(f'O {n2} é maior')

### Questão 02
Letra = str(input('Digite sua letra: '))

if Letra =='a' or Letra =='e' or Letra =='i' or Letra =='o' or Letra =='u' or \
    Letra =='A' or Letra =='E' or Letra =='I' or Letra =='O' or Letra =='U':
    print(f'A letra ({Letra}) é vogal...')
else:
    print(f'A letra ({Letra}) não é vogal...')

### Questão 03
Turno = str(input('Digite seu turno Manhã(A), Tarde(T), Noite(N) / [A,T,N,]: '))
if Turno == 'A' or Turno == 'a':
    print('Bom Dia!')
elif Turno == 'T' or Turno == 't':
    print('Boa Tarde!')
else:
    print('Boa Noite!')

### Questão 04
Num = int(input('Digite seu número: '))
if Num % 2 == 0:
    print(f'O número {Num} é par...')
else:
    print(f'O número {Num} é impar...')

### Questão 05
while True:
    nun = int(input('Informe um número para exibir sua tabuada [0 p/ sair]: ')) #achei mais interessante usar o zero para sair.
    if nun == 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        print(f'{nun} x {cont:2} = {nun * cont:3}')
print('Programa encerrado. Volte sempre!')

### Questão 06

for i in range(1000,2001):
    if i % 11 == 2:
        print(i)

### Questão 07

num = int(input("Insira o tamanho do quadrado: "))

for i in range(num):
    print()
    for j in range(num):
        print("*",end = '')

### Questão 08

n = int(input('Insira o tamanho do triangulo: '))    # Número de linhas no triângulo
num = 1    # Contador inicial

for i in range(1, n + 1): # Loop para o número de linhas
    print()
    for j in range(1, i + 1):   # Loop para os números em uma linha
        print("*", end=' ')
        num += 1
    print()


### Estudar... Biblioteca turtle
import turtle
tortuga=turtle.Turtle()

def sierp(x,y):
        if y==0:
                tortuga.shape("turtle")
                tortuga.color("green")
                tortuga.begin_fill()
                tortuga.forward(x)
                tortuga.left(120)
                tortuga.forward(x)
                tortuga.left(120)
                tortuga.forward(x)
                tortuga.left(120)
                tortuga.end_fill()
        else:
                sierp(x/2,y-1)
                tortuga.forward(x/2)
                sierp(x/2,y-1)
                tortuga.left(120)
                tortuga.forward(x/2)
                tortuga.right(120)
                sierp(x/2,y-1)
                tortuga.right(120)
                tortuga.forward(x/2)
                tortuga.left(120)

window = turtle.Screen()
tortuga.speed(3)
sierp(200,3)
window.exitonclick()

