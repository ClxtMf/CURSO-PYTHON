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
