var1 = int(input('Informe um valor: '))
var2 = input('Informe um valor: ')
var3 = float(input('Informe um valor: '))
var4 = bool(input('Informe um valor: '))

lista = [var1, var2, var3, var4]

def exibirLista(lst):

    print(f'Exibindo a lista {lst}')

exibirLista(lista)

"""""""""""""""""""""""""""""""""""""""""""""""""

cursos = ['dev Full Stack', 'Python', 'fotoxopi']

print(f'Nossos cursos são: {cursos}')
print('--------------------------------\n\n')

cursos[2] = 'Photoshop'

print(f'Nossos cursos são: {cursos}\n\n')

print(cursos[0])

"""""""""""""""""""""""""""""""""""""""""""""""""""
lista01 = [10, 20, 30]
lista02 = [40, 50, 60]
def somar(lista01,lista02):
    print(f'Lista 1 mais lista 2: {lista01[0] + lista02[2]}')
somar(lista01,lista02)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista = [10, 20, 30, 40, 50]
def somar(lista):
    print(f'O valor da soma dos itens da lsita é: {sum(lista)}')
somar(lista)
