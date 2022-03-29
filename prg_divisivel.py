num = int(input("Entre com um numero: "))
r1 = num % 10
r2 = num % 5
r3 = num % 2
if r1 == 0 :
    print ("Esse numero é multiplo de 10")
else :
    if r3 == 0 :
        print ("Esse numero é multiplo de 2")
    else :
        if r2 == 0 :
            print ("Esse numero é multiplo de 5")
        else :
            print ("Esse numero nao é multiplo de 5 e 2")
    print ("Esse numero nao é multiplo de 10")