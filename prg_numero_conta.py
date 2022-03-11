conta = int(input("Digite o numero da conta de três digitos: "))
d1 = int(conta / 100)
d2 = int(conta % 100 / 10)
d3 = int(conta % 100 % 10)
inv = d3 * 100 + d2 * 10 + d1
soma = conta + inv
d1 = int(soma / 100) * 1
d2 = int(soma % 100 / 10) * 2
d3 = int(soma % 100 % 10) * 3
digito = int((d1+d2+d3) % 10)
print ("O digito verificador da conta é: ",digito)
print ("O numero da conta é: ",conta,"-",digito)
