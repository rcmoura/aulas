a = float(input("Digite o 1o. Numero: "))
b = float(input("Digite o 1o. Numero: "))
c = float(input("Digite o 1o. Numero: "))
if a > b:
    if c > a:
        maior = c
        intermediario = a
        menor = b
    else:
        if c > b:
            maior = a
            intermediario = c
            menor = b
        else:
            maior = a
            intermediario = b
            menor = c
else:
    if c > b:
        maior = c
        intermediario = b
        menor = a
    else:
        if c > a:
            maior = b
            intermediario = c
            menor = a
        else:
            maior = b;
            intermediario = a;
            menor = c;
print ("Maior: ",maior)
print ("Intermediario: ",intermediario)
print ("Menor, ",menor)