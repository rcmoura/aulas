# inicializa o vetor de notas com 0
notas = [0] * 5
soma = 0
#preeche vetor de notas sem usar append
for i in range(5):
    notas[i] = eval(input('Digite a nota do aluno '+ str(i) +': '))
    soma = soma + notas[i]

media = soma / 5
print ('A media da turma é: ', media)