
lista = [8,75,4,3,2,1,90,123,543,76,1]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        left = [x for x in lista[1:] if x <= pivot]
        right = [x for x in lista[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(lista))
