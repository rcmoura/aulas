ha = float(input("Entre com as horas tralhadas: "))
vha = float(input("Entre com o valor da hora trabalhada: "))
pd = float(input("Entre com o percentual do INSS: "))
sb = ha * vha
td = (pd / 100) * sb
sl = sb - td
print ("Salario liquido: ", sl)