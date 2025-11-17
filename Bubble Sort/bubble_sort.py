def bubble_sort(arreglo:list, desc)-> list:
    if not desc:
        for i in range(len(arreglo) - 1):
            for j in range(i + 1, len(arreglo)):
                if arreglo[i] > arreglo[j]:
                    temp = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = temp
    else:
        for i in range(len(arreglo) - 1):
            for j in range(i + 1, len(arreglo)):
                if arreglo[i] < arreglo[j]:
                    temp = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = temp

    return arreglo

numeros = [8,4,-2,11,9]
print(numeros)
numeros = bubble_sort(numeros, False)
print(numeros)

# ¿Cómo es que me permite ordenar mayor a menor el array de números?
# ¿Qué debería cambiar si quisiera ordenar con otro criterio (menor a mayor)?
# ¿Qué es un intercambio o swap?
