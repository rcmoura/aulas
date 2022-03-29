import math

a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))
if a == 0 :
    print ("Não é uma equação de 2 grau!!")
else :
    d = b**2 - 4 * a * c;
    if d >= l0 :
        d = math.sqrt(d)
        x1 = (-b + d) / (2 * a);
        x2 = (-b - d) / (2 * a);
        print ("x1 = ",x1," x2 = ",x2)
    else :
        print ("Não há raizes reais") 