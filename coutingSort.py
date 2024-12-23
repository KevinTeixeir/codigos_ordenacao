def counting_sort(lista):
    if not lista:
        return lista #Retorna se a lista estiver vazia

    #Encontrando o valor máximo da lista
    valor_max = max(lista)
    count = [0] * (valor_max + 1) #Inicializando uma lista de contagem com zeros

    while len(lista) > 0:
        #Removendo o primeiro elemento da lista e o armazenando na variável num
        num = lista.pop(0) 

        #contando a quantidade de vezes que cada número aparece na lista original
        count[num] += 1 

    #construindo a lista ordenada com base nas contagens.
    for i in range(len(count)):
        
        while count[i] > 0:
            lista.append(i)
            count[i] -= 1

    return lista

#Exemplo
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]

print(f"\nlista antiga: {lista}")
lista_ordenada = counting_sort(lista)
print(f"\nLista ordenada: {lista_ordenada}\n")

