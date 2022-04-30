alunos = [['josé.','Dev'], ['Fco.','Fotografia'], ['Luana.','Marketing'], ['Maria.','Dev']]

for item in alunos:
    for aluno in item:
        print(aluno)
        
""""""""""""""""""""""""""""""""""""""""""""""""

alunos = []
for i in range(3):
    aluno = []
    for j in range(1):
        a = input('Informe o nome dos alunos: ')
        c = input('Informe o curso do aluno: ')
        aluno.append(a)
        aluno.append(c)
    alunos.append(aluno)
    print(alunos)
