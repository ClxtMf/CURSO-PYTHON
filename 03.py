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
