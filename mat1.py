# Matriz também conhecida como variável composta multidimensional
turma = [[5,4.5,7,5.2,6.1],[2.1,8,6.5,7,6.7],[8.6,7,9.1,8.7,9.3]]
#calcula a média
media = 0
#for para percorrer as linhas
for i in range(3):
    #for para percorrer as colunas
    for j in range(5):
        media = media + turma[i][j]
media = media / 15
print(media)