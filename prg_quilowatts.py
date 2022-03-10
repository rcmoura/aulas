sm = float(input("Entre com o salário minimo: "))
qtdade = float(input("Entre com a quantidade de quillowatts: "))
# divide por 7 para achar o presso de 100kw e por 100 achar de 1kw
preco = float(sm/700)
vp = float(preco*qtdade)
# vd = float(vp-(vp * 0.1))
vd = float(vp * 0.9)
print("Preço do quilowatt: ",preco," valor a ser pago: ",vp," Valor com desconto: ",vd)