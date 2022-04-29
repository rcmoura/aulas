l1 = float(input("Digite o 1o. Lado: "))
l2 = float(input("Digite o 2o. Lado: "))
l3 = float(input("Digite o 3o. Lado: "))
a = float(l2 + l3)
b = float(l1 + l3)
c = float(l1 + l2)
if l1 < a and l2 < b and l3 < c :
    if a == b and a == c:
        print ("Triangulo Equilatero")
    else :
        if  a == b or a == c or b==c: 
            print ("Triangulo Isosceles")
        else:
            print ("Triangulo Escaleno")
else:
    print ("As medidas não formam um triangulo")