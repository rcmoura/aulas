a = float(input("Digite o 1o. Numero: "))
b = float(input("Digite o 1o. Numero: "))
c = float(input("Digite o 1o. Numero: "))
if a > b:
    aux = a
    a = b
    b = aux
if a > c:
    aux = a
    a = c
    c = aux
if b > c:
    aux = b
    b = c
    c = aux
maior = c
intermediario = b
menor = a
print ("Maior: ",maior)
print ("Intermediario: ",intermediario)
print ("Menor, ",menor)