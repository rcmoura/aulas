# programa calculadora
print("+ para Somar")
print("- para Subritair")
print("* para Multiplicar")
print("/ para Dividir")
resp = input ("Digitar opção: ")
if resp == "+":
    a = float(input("Digite 1o numero: "))
    b = float(input("Digite 2o numero: "))
    soma = float(a + b)
    print ("Soma: ",soma)
else:
    if resp == "-":
        a = float(input("Digite 1o numero: "))
        b = float(input("Digite 2o numero: "))
        sub = float(a - b)
        print ("Subtração: ",sub)
    else:
        if resp == "*":
            a = float(input("Digite 1o numero: "))
            b = float(input("Digite 2o numero: "))
            mult = float(a * b)
            print ("Multiplicação: ",mult)
        else:
            if resp == "/":
                a = float(input("Digite 1o numero: "))
                b = float(input("Digite 2o numero: "))
                if a == 0:
                    print ("Não é possivel dividir por 0")
                else:  
                    divide = float(a / b)
                    print ("Divisão: ",divide)
            else:
                print ("Opção indisponivel")
