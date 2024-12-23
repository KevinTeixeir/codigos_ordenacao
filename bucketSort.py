def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Encontra o valor máximo e mínimo na lista
    max_val = max(arr)
    min_val = min(arr)
    
    # Cria um número de buckets apropriado
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribui os elementos nos buckets
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
        buckets[index].append(num)
    
    # Ordena cada bucket e junta os resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    # Copia a lista ordenada de volta para o array original
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

# Teste com uma lista de exemplo para Bucket Sort
teste_lista = [3, 6, 8, 10, 1, 2, 1]
bucket_sort(teste_lista)
print("Lista original:", [3, 6, 8, 10, 1, 2, 1])
print("Lista ordenada:", teste_lista)
