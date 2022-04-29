h = float(input("Entre com a Altura: "))
s = input("Entre com o sexo M / F -> ")
if s == 'M' or s == 'm':
    peso = 72.7 * h - 58
else :
    peso = 62.1 * h - 44.7
print ("Seu peso ideal é: ", peso)
