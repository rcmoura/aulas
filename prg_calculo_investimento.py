deposito = float(input("Deposito inicial: "))
taxa = float(input("Taxa de juros: "))
investimento = float(input("Deposito mensal: "))
mes = int(input("Entre com o numero de meses: "))
render = 1
saldo = deposito
while render <= mes:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print (f"Saldo do mês {render} é de R${saldo:5.2f}.")
    render = render + 1
valor_obtido = saldo - deposito
print(f"O ganho obtido com os juros foi de R${valor_obtido:8.2f}.")