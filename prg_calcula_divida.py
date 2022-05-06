divida = float(input("Sua divida: "))
taxa = float(input("Taxa de juros: "))
Pagamento = float(input("Pagamento mensal: "))
mes = 1
tristeza = divida * (taxa / 100)
if tristeza > Pagamento:
    print("Sua divida não será paga nunca, pois os juros são superiores ao pagamento mensal")
else:
    saldo = divida
    juros_pago = 0
    while saldo > Pagamento:
        juros = saldo * taxa / 100
        saldo = juros_pago + juros - Pagamento
        juros_pago = juros_pago + juros
        print(f"Saldo da divida no mes {mes} é de R${saldo:6.2f}")
        mes = mes + 1
    print(f"Para pagar uma divida de R${divida:8.2f}, a {taxa:5.2f} % de juros, ")
    print(f"você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros")
    print(f"No ultimo mes, voce teria um saldo residual de R${saldo:8.2f} a pagar")