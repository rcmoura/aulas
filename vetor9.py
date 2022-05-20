a = []
b = []
c = []

for i in range(1,16):
    a.append(int(input('Informe p {}º valor do vetor A: '.format(i))))
for i in range(1,16):
    b.append(int(input('Informe p {}º valor do vetor B: '.format(i))))
c = a + b
for x in range(0, 30):
    print('C[{}] = {}'.format(x + 1, c[x]))
