def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
            
teste_lista = [3, 6, 8, 10, 1, 2, 1]
merge_sort(teste_lista)
print("Lista original:", [3, 6, 8, 10, 1, 2, 1])
print("Lista ordenada:", teste_lista)
