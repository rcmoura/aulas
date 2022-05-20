a = []
b = []
for i in range(0,5):
    a.append(float(input("Informe o {}º Valor em graus Celsius no vetor A: ".format(i + 1))))
for i in range(0,5):
    b.append(a[i] * 1.8 + 32)
for i in range(0,5):
    print('A[{}] = {}ºC igual a B[{}] = {}ºF'.format(i, a[i],i,b[i]))
