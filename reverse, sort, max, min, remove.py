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
