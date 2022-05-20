a=[]
b=[]
for i in range(0,15):
    a.append(int(input('informe o {}º valor de A: '.format(i+1))))
for i in range(0,15):
    b.append(1)
    for y in range(1, a[i]):
        b[i] = b[i] * y
    b.append(b[i])
print ('_____________________________________________')
for z in range(0,15):
    print('{}! é igual a {}'.format(a[z], b[z + 1]))
print ('_____________________________________________')