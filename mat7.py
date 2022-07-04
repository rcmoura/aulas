m = []
#preencher a matriz
for i in range(5):
    linha = []
    linha.append(input('Digite o nome da pessoa ' + str(i) + ': '))
    linha.append(int(input('Digite a idade de ' + linha[0] + ': ')))
    m.append(linha)
#procurar a pessoa mais nova
menor = m[0][1]
pos = 0
for i in range(5):
    if m[i][1] < menor:
        menor = m[i][1]
        pos = i
#imprime a matriz
for i in range(5):
    print(m[i])
print ('A pessoa mais nova é ', m[pos][0])