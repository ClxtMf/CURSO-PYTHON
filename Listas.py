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

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.pop()

del(lista[0:6:2])

print(lista)
'''
# reverse, sort, max, min, remove
'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.reverse()
print('Lista reversa: ',lista)

lista.sort()
print('Lista em ordem crescente:', lista)

print('Maior valor: ',max(lista))
print('Menor valor: ', min(lista))

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


lista01 = [10, 20, 30]
lista02 = [40, 50, 60]


def somar(lista01, lista02):
    print(f'Lista 1 mais lista 2: {lista01[0] + lista02[2]}')


somar(lista01, lista02)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista03 = [10, 20, 30, 40, 50]


def somar(lista03):
    print(f'O valor da soma dos itens da lsita é: {sum(lista03)}')


somar(lista03)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista = [1, 2, 3, 4]

def concatenar(x):
    return x + x

novaLista = concatenar(lista)
print(novaLista)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(f'O valor de item: {item}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
usuarios = ['zezim1337', 'paulimheadshot', 'mamute1337']

print('Lista: ', usuarios)

user = input('Insira o nome do novo usuário: ')

usuarios.append(user)

print(f'Lista atualizada: {usuarios}')

Novo_Usúario = input('informe o nome do novo usúario: ')
usuarios.insert(1, Novo_Usúario)
print(f'Lista atualizada 2: {usuarios}')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista001 = []
def add():
    for Num in range(5):
        i = int(input('Informe os valores: '))
        lista001.append(i)
        print(f'Os valores são: {lista001}')
add()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lista_Média = []
def Média():
    for i in range(3):
        var = int(input('Informe as notas: '))
        lista_Média.append(var)
        print(f'As notas são: {lista_Média}')
        print(f'A média das notas somadas é: {sum(lista_Média) / 3}')
Média()


letra = ''
lista = []
for i in range(10):
    letra = input('Informe uma letra: ')
    if len(letra) > 1:
        print('Digite apenas um caractere: ')
        continue
    else:
        lista.append(letra)


def contarConsoantes(lista):
    cons = 0
    for item in lista:
        if item.lower() not in 'aeiou':
            cons += 1

    print(f'Quantidade de consoantes: {cons}')


contarConsoantes(lista)
