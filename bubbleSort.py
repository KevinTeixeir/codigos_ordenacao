import random
import time
ini = time.time()
def bubbleSort(lista):
    n = len(lista)
    for j in range(n-1,0,-1):
        for i in range(j):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = []
for i in range(1, 10000):
    lista.append(random.randint(0,10000))
bubbleSort(lista)
print(lista[1:-1])
fim = time.time()
tempo = fim - ini
print(f"tempo: {tempo:.2f}")