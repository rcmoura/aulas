def maior(vetor):
    if len(vetor) > 1:
        for j in range(0,len(vetor)):
            for i in range(0,len(vetor)-1):
                if vetor[i]>vetor[i+1]:
                    aux = vetor[i+1]
                    vetor[i+1] = vetor[i]
                    vetor[i]= aux
    return vetor[len(vetor)-1]

def menor(vetor):
    if len(vetor) > 1:
        for j in range(0,len(vetor)):
            for i in range(0,len(vetor)-1):
                if vetor[i]<vetor[i+1]:
                    aux = vetor[i+1]
                    vetor[i+1] = vetor[i]
                    vetor[i]= aux
    return vetor[len(vetor)-1]

v = [5,4,2,1,10,78,9,7,55]
print(v)
m = maior(v)
print(m)
print(v)
n = menor(v)
print(n)
print(v)