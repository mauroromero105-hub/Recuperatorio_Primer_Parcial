def bubble_sort(arreglo:list, desc = False) -> list:
    if not desc:
        #Ordenamiento por burbujeo ascendente
        for i in range(len(arreglo) - 1):
            for j in range(i + 1, len(arreglo)):
                if arreglo[i] > arreglo[j]:
                    temp = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = temp
    else:
        #Ordenamiento por burbujeo descendiente
        for i in range(len(arreglo) - 1):
            for j in range(i + 1, len(arreglo)):
                if arreglo[i] < arreglo[j]:
                    temp = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = temp

    return arreglo

numeros = [8,4,-2,11,9]
print(numeros)
numeros = bubble_sort(numeros, True)
print(numeros)