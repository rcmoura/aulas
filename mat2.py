turma = []
for i in range(3):
    # cria linha vazia
    linha = []
    for j in range(5):
        #vai adcionando as notas na linha
        linha.append(int(input('Digite a nota ['+ str(i) + ',' + str(j) + ']: ')))
        turma.append(linha)