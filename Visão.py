'''
OPERADORES RELACIONAIS

!=  DIFERENTE 2 != 3
==  IGUAL 2 == 2
>   MAIOR QUE 3 > 2
>=  MAIOR QUE OU IGUAL A 3 >= 3
<   MENOR QUE 3 < 4
<=  MENOR QUE OU IGUAL A 4 <= 4



print(2 != 3)
print(2 == 2)
print(3 > 2)
print(3 > 3)
print(3 >= 3)
print(4 <= 4)


ESTRUTURAS DE SELEÇÃO OU CONTROLE DE FLUXO

if
else



#EM OUTRAS LINGUAGENS
if (3 > 4){

}

#EM PYTHON

if 5 > 4:
    print("A condição é Verdadeira")
    var = 4
    print(var)
else:
    print("A condição NÃO é verdadeira")


if 5 > 6:
    print("A condição é Verdadeira")
    var = 4
    print(var)
else:
    print("A condição NÃO é verdadeira")


1 - LEIAM DOIS NÚMEROS E IMPRIMA O MAIOR DELES
2 - LEIA UMA IDADE E INFORME SE O USUÁRIO É MAIOR DE IDADE OU NÃO
3 - LEIA UM NÚMERO E INFORME SE ELE É PAR OU IMPAR
4 - LEIA UMA ALTURA E SE A ALTURA FOR INFERIOR A 1.50 INFORME QUE ELE NÃO PODERÁ ENTRAR NO BRINQUEDO
5 - VERIFIQUE UMA SENHA FORNECIDA PELO USUÁRIO (SENHA = 12345) SE ELE FOR IGUAL A 12345 INFORME QUE O ACESSO É PERMITIDO, SENÃO INFORME QUE O ACESSO ESTÁ NEGADO


###EXEMPLO 01
##RESOLUÇÃO DO PROFESSOR

valor1 = input('Digite um valor: ')
valor1 = int(valor1)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor1 > valor2:
print(f"O maior valor é: {valor1}")
else:
print(f'O maior valor é: {valor2}')

##MEU CÓDIGO

n1 = int(input("Digite um Número "))
n2 = int(input("Digite outro Número "))

if n1 > n2:
    print('Este é o Maior', n1)
else:
    print("Este é o Maior", n2)

###EXEMPLO 02
##RESOLUÇÃO DO PROFESSOR

idade = int(input('Informe a sua idade: '))
if idade >= 18:
print('Você é maior de idade')
else:
print('Você não é maior de idade')

##MEU CÓDIGO

Idade = int(input('Informe sua idade: '))
if Idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

###EXEMPLO 03
##RESOLUÇÃO DO PROFESSOR

num = int(input('Digite um número: '))
if num %2 == 0:
print("O valor é Par")
else:
print("O valor é Ímpar")


##MEU CÓDIGO
numero = int(input("Informe um número: "))

if numero %2 == 0:
    print('Par')
else:
    print('Ímpar')

###EXEMPLO 04
##RESOLUÇÃO DO PROFESSOR

altura = float(input('Informe a sua altura: '))
if altura < 1.50:
print("Você tem altura suficiente")
else:
print("Você não tem altura suficiente")

##MEU CÓDIGO

altura = float(input('Informe sua Altura: '))

if altura >= 1.50:
    print('Liberado')
else:
    print('Negado')

###EXEMPLO 05
##RESOLUÇÃO DO PROFESSOR

senha = input('Digite sua senha: ')
if senha == '12345':
print('Acesso permitido!')
else:
print("Acesso negado!")


##MEU CÓDIGO # 12345 != '12345'

senha = int(input('Informe sua senha: '))

if senha == 12345: #errado, não podemos utilizar sem as aspas por que um codigo numerico sem aspas é um inteiro e com é string.
    print('Acesso Concedido')
else:
    print('Acesso Negado')


#OPERADORES LÓGICOS AND/OR/NOT
##EX01
altura = 1.66
vestep = altura > 1.30 and altura < 1.70
print(vestep)

altura = 1.71
vestep = altura > 1.30 and altura < 1.70
print(vestep)

##EX02

estudante = True
professor = False
meia_entrada = estudante == True or professor == True
print(meia_entrada)

estudante = False
professor = False
meia_entrada = estudante == True or professor == True
print(meia_entrada)

##EX03

estudante = True
professor = False
meia_entrada = not (estudante == True) or professor == True
print(meia_entrada)

#elif OU else if

idade = int(input("Digite sua idade: "))
#idade < 12 ---- 100% de desconto
#idade >= 12 e idade < 17 ---- 50% de desconto
#idade >= 17 e idade < 22 ---- 25% de desconto
#idade >= 22 ---- 0% de desconto

if idade < 12:
    print('Você tem 100% de desconto')
elif idade >= 12 and idade < 17: #else if (se não, se) - elif
    print('Você tem 50% de desconto')
elif idade >= 17 and idade < 22:
    print('Você tem 25% de desconto')
else:  #Como essa é a ultima linha para testar, utiliza-se o 'else'.
    print('Você não tem desconto')
'''
'''
ARENA CASTELÃO

categoria - professor, estudante, pcd, nenhum
faixa salario - 0 -1000, 1001 - 2000, 3000
idade - 0 a 12, 13 a 22, 23 - 60

vip - pcd, salario > 3000 idade 60
camarote - professor, estudante salario até 2000
pista - nenhum, 0 -1000, idade 13 a 22



categoria = int(input("Informe sua categoria: " \
                     "1 - professor " \
                     "2 - estudante " \
                     "3 - pcd " \
                     "4 - nenhum: "))
faixa_sal = float(input("Informe o seu salario: "))
idade = int(input('Informe a sua idade: '))

if categoria == 3 or faixa_sal > 3000 or idade > 60:
    print('Você vai para area VIP!')
elif categoria == 1 or categoria == 2 or faixa_sal < 2000:
    print('Você vai para o Camarote!')
else:
    print('Você vai pra pista!')
'''
'''
1 - LER UMA HORA (int)
hora > 6 entre 6 e 11 (imprmir bom dia)
hora entre 12 e 17 (imprimir boa tarde)
hora entre 18 até as 23 (imprimir boa noite)
hora entre 23 e 5 (imprimir boa madrugada)

2 - LER TRÊS NOTAS E FAZER A MÉDIA
SE MEDIA FOR MAIOR QUE 9 IMPRIMIR APROVADO COM LOUVOR
IF A MEDIA FOR MAIOR QUE 7 E MENOR QUE 9 IMPRIMIR APROVADO
SE MÉDIA FOR MAIOR QUE 4 E MENOR QUE 7 IMPRIMIR RECUPERAÇÃO
SE A MEDIA FOR MENOR QUE 4 IMPRIMIR REPROVADO DIRETO

3 - FAÇA UM PROGRAMA QUE LEIA A ALTURA E O PESO DE UM USUÁRIO E CALCULE O SEU IMC - imc = peso % altura ao quadrado
IMC = PESO / ALTURA * ALTURA
IMC < 18.5 = MAGREZA
IMC ENTRE 18.5 E 24.9 = NORMAL
IMC ENTRE 25 E 29.0 = SOBREPESO
IMC ENTRE 30 E 39.9 = OBESIDADE
IMC MAIOR QUE 40 = OBESIDADE MORBIDA

4 - ESCREVA UM PROGRAMA QUE LEIA AS MEDIDAS DE UM LADO DE UM TRIANGULO E DE ACORDO COM ESSAS MEDIDAS INFORMAR SE O TRIANGULO É ISÓCELES, EQUILÁTERO OU ESCALENO.
EQUILATERO - TODOS OS LADOS IGUAIS
ISOCELES - DOIS LADOS IGUAIS
ESCALENO - TODOS OS LADOS DIFERENTES

'''

###EXERCICIO 01
hora = int(input("Que horas são?: "))
#hora > 6 entre 6 e 11 (imprmir bom dia)
#hora entre 12 e 17 (imprimir boa tarde)
#hora entre 18 até as 23 (imprimir boa noite)
#hora entre 23 e 5 (imprimir boa madrugada)
if hora >= 6 and hora < 12:
    print('Bom dia!')
elif hora >= 12 and hora < 18:
    print('Boa tarde!')
elif hora >= 18 and hora < 24:
    print('Boa noite!')
elif hora >= 0 and 5:
    print('Boa Madrugada')
