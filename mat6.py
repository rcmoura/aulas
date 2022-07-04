matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite a nota ['+ str(i) + ',' + str(j) + ']: ')))
    matriz.append(linha)
#contar pares
pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares = pares + 1
#imprimir em formato de matriz
for i in range(3):
    print(matriz[i])
#imprimir qtde de numeros pares
print ('A matriz contem ',pares,' numeros pares')