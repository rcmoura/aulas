# eup  que exiba a soma de todos os números pares entre dois números quaisquer, incluindo-os

num1 = int(input('Entre com o valor inicial: '))
num2 = int(input('Entre com o valor final: '))
soma = 0
for i in range(num1,num2 + 1):
    resto = i % 2
    if resto == 0:
        soma = soma + i
print ("A soma é: ", soma)