
import random
import time
ini = time.time()
def insertion_sort(lista):
    n= len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1]= lista[j]
            j = j-1
        lista[j+1]=chave
    return lista

lista = []
for i in range(1, 100000):
    lista.append(random.randint(1,100000))
print(insertion_sort(lista[1:-1]))
fim = time.time()
tempo = fim - ini
print(f"tempo: {tempo:.2f}")