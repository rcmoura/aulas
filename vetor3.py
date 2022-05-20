num_alunos = 5
nomes = []
notas = []
media = 0

for i in range(num_alunos):
    nomes(input('Informe o nome do aluno: '))
    notas.append(eval(input('Informe a nota de '+ nomes[i] +': ')))
    media = media + notas[i]

media = media / num_alunos
print('A media da turma é: ',media)

for i in range(num_alunos):
    if notas[i] > media:
        print('Parabens', nomes[i])