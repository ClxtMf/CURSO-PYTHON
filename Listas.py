lista_Vazia = []
print(f'Lista Vazia: {lista_Vazia}')
print(f'Tipo da Lista: {type(lista_Vazia)}')


Lista_Inteiros = [1, 4, 5, 7, 8, 9]
print(f'Valores contados na lista: {Lista_Inteiros}')


lista_tipos_diferentes = ['Brasil', 5, 'Titulos']
print(F'{lista_tipos_diferentes} ')


Nome = 'Infinity'
Inteiro = 100
Flutuante = 2.58
Booleano = True
lista_Varios_tipos = [Nome, Inteiro, Flutuante, Booleano]
print(f'{lista_Varios_tipos}')

Lista_Função = [10, 20, 30, 40, 50]
def lista(Lista_Função):
    print(f'Os valores são: {Lista_Função}')

lista(Lista_Função)




var1 = int(input('Informe um valor: '))
var2 = input('Informe um valor: ')
var3 = float(input('Informe um valor: '))
var4 = bool(input('Informe um valor: '))

lista = [var1, var2, var3, var4]

def exibirLista(lst):

    print(f'Exibindo a lista {lst}')

exibirLista(lista)




cursos = ['dev Full Stack', 'Python', 'fotoxopi']

print(f'Nossos cursos são: {cursos}')
print('--------------------------------\n\n')

cursos[2] = 'Photoshop'

print(f'Nossos cursos são: {cursos}\n\n')

print(cursos[0])





lista01 = [10, 20, 30]
lista02 = [40, 50, 60]
def somar(lista01,lista02):
    print(f'Lista 1 mais lista 2: {lista01[0] + lista02[2]}')
somar(lista01,lista02)




lista = [10, 20, 30, 40, 50]
def somar(lista):
    print(f'O valor da soma dos itens da lsita é: {sum(lista)}')
somar(lista)
