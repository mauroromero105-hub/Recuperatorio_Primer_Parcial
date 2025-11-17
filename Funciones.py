from Inputs import*

def mostrar_menu():
    print(f"1.Cargar nombre y apellido\n2.Cargar calificaciones\n3.Mostrar calificaciones\n4.Mostrar participantes con promedio mayor a 4\n5.Mostrar participantes con promedio mayor a 8\n6.Jurado más estricto\n7.Mostrar ganador\n8.Buscar participante por apellido\n9.Salir")

def crear_array(cantidad_elementos:int, valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

def crear_matriz(cantidad_filas:int,cantidad_columnas:int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [None] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_calificaciones(array_participantes:list, matriz_calificacion) -> bool:
    retorno = False
    if type(matriz_calificacion) == list and len(matriz_calificacion) > 0 and type(array_participantes) == list and len(array_participantes) > 0:
        for i in range(len(array_participantes)):
            if type(matriz_calificacion[i]) == list:
                mostrar_calificacion(array_participantes,matriz_calificacion,i)
                retorno = True
    return retorno

def mostrar_nombre(cadena:str) -> str:
    if type(cadena) == str and len(cadena) > 0:
        nombre=""
        apellido=""
        espacio_encontrado = 0
        for i in range(len(cadena)):
            auxiliar = cadena[i]
            codigo = ord(auxiliar)

            if codigo == 32:
                espacio_encontrado += 1
                auxiliar = ""

            if espacio_encontrado == 0:
                nombre = nombre + auxiliar
            else:
                apellido = apellido + auxiliar
        nombre_completo = print(f"\nNombre: {nombre}\nApellido: {apellido}")

    return nombre_completo

def mostrar_calificacion(array_participante:list,matriz_calificacion:list,indice:int) -> bool:
    retorno = False
    if type(matriz_calificacion) == list and len(matriz_calificacion) > 0 and type(array_participante) == list and len(array_participante) > 0 and type(matriz_calificacion[indice]) == list:
        promedio = suma_y_promedio(matriz_calificacion, indice, "col")
        mostrar_nombre(array_participante[indice])
        for col in range(len(matriz_calificacion[indice])):
            print(f"JURADO {col + 1}: {matriz_calificacion[indice][col]}")
        print(f"PROMEDIO: {promedio:.2f}/10")
        retorno = True

    return retorno

def sumar_calificaciones(matriz:list,indice:int, modo:str) -> int | float:
    suma = 0
    
    if type(modo) == str:
        if modo == "col":
            if type(matriz) == list and indice < len(matriz) and indice >= 0:
                if type(matriz[indice]) == list:
                    for col in range(len(matriz[indice])):
                        if type(matriz[indice][col]) == int or type(matriz[indice][col]) == float:
                            suma += matriz[indice][col]
        elif modo == "fil":
            if type(matriz) == list:
                for fil in range(len(matriz)):
                    if indice < len(matriz[fil]) and indice >= 0 and type(matriz[fil]) == list:
                        if type(matriz[fil][indice]) == int or type(matriz[fil][indice]) == float:
                            suma += matriz[fil][indice]
        else:
            print("Error, elija fil(fila) o col(columna)")
    else:
        print("Error, caracter invalido(Solo letras)")

    return suma

def calcular_promedio(matriz: list, indice: int, total: float, modo:str) -> float:
    cantidad = 0
    if type(matriz) == list and len(matriz) > 0:

        if type(modo) == str:
            if modo == "col":
                cantidad = len(matriz[indice])
            elif modo == "fil":
                cantidad = len(matriz)
            else:
                print("Error, elija fil(fila) o col(columna)")
        else:
            print("Error, caracter invalido(Solo letras)")

    promedio = total / cantidad
    return promedio

def suma_y_promedio(matriz: list, indice:int, modo:str) -> float:
    if type(matriz) == list and len(matriz) > 0:
        suma_total = sumar_calificaciones(matriz, indice, modo)
        promedio = calcular_promedio(matriz, indice, suma_total, modo)
    return promedio

def mayor_a(array:list, matriz:list, consigna:int) -> bool:
    retorno = False
    cantidad = 0
    for i in range(len(array)):
        promedio = suma_y_promedio(matriz, i, "col")
        if promedio > consigna:
            cantidad += 1
            mostrar_calificacion(array, matriz, i)
            retorno = True
    if cantidad == 0:
        print(f"No hay participantes con promedio mayor a {consigna}")
        retorno = True
    return retorno

def calcular_jurado_estricto(matriz:list) -> int | float:
    bandera = False
    
    for col in range(len(matriz[0])):
        promedio = suma_y_promedio(matriz, col, "fil")
        
        if bandera == False:
            minimo = promedio
            bandera = True
        else:
            if promedio < minimo:
                minimo = promedio
    
    return minimo

def calcular_ganador(matriz:list) -> float:
    bandera = False

    for fil in range(len(matriz)):
        promedio = suma_y_promedio(matriz, fil, "col")
        
        if bandera == False:
            maximo = promedio
            bandera = True
        else:
            if promedio > maximo:
                maximo = promedio
    return maximo

def mostrar_jurado_estricto(matriz_votos:list) -> bool:
    if type(matriz_votos) == list:
        retorno = True
        valor_minimo = calcular_jurado_estricto(matriz_votos)
        
        print("El/Los jurado/s más estricto/s: ")
        for fil in range(len(matriz_votos)):
            promedio_jurado = suma_y_promedio(matriz_votos, fil, "fil")
            if promedio_jurado == valor_minimo:
                    print(f"\nEl JURADO {fil + 1}: {promedio_jurado:.2f}")
    else:
        retorno = False

    return retorno

def mostrar_ganador(array_participantes:list, matriz_votos:list) -> bool:
    if type(matriz_votos) == list and len(matriz_votos) > 0 and type(array_participantes) == list and len(array_participantes) > 0:
        retorno = False
        valor_maximo = calcular_ganador(matriz_votos)
        print(f"La nota promedio más alta es de: {valor_maximo:.2f}")

        ganadores = [None]
        indice = 0

        for fil in range(len(matriz_votos)):
            if suma_y_promedio(matriz_votos, fil, "col") == valor_maximo:
                ganadores[indice] = array_participantes[fil]
                nuevo = [None] * (len(ganadores) + 1)
                for i in range(len(ganadores)):
                    nuevo[i] = ganadores[i]
                ganadores = nuevo
                mostrar_calificacion(array_participantes, matriz_votos, fil)
                indice += 1

        if indice > 1:
            print("\nHUBO UN EMPATE, SE DEFINIRÁ EN UNA RONDA EXTRA")
        else:
            print(f"\nEL GANADOR ES: {ganadores[0]}")
        retorno = True
    else:
        retorno = False
    return retorno

def convertir_minuscula(caracter:str) -> str:
    codigo = ord(caracter)
    if 65 <= codigo <= 90:     
        return chr(codigo + 32)
    return caracter

def encontrar_coincidencias(texto:str, patron:str) -> bool:
    if len(patron) > len(texto):
        return False

    for i in range(len(patron)):
        encontrado = convertir_minuscula(texto[i])   
        coincidencia = convertir_minuscula(patron[i])  
        if encontrado != coincidencia:
            return False

    return True

def conseguir_apellido(nombre_completo:str) -> str: 
    apellido = ""
    espacio_encontrado = 0
    caracteres_apellido = 0

    for i in range(len(nombre_completo)):
        auxiliar = nombre_completo[i]
        codigo = ord(auxiliar)

        if codigo == 32:
            espacio_encontrado = 1
            continue

        if espacio_encontrado == 1:
            apellido = apellido + auxiliar
            caracteres_apellido += 1

    if espacio_encontrado == 0 or caracteres_apellido == 0:
        print("Error: no se encontró el apellido.")
        
    return apellido

def buscar_apellido(array_participantes:list, matriz_votos:list) -> bool:
    retorno = False
    while retorno == False:
        patron = input("Ingrese apellido o parte del apellido: ")

        resultados = [None]
        coincidencias = 0

        for i in range(len(array_participantes)):
            
            apellido = conseguir_apellido(array_participantes[i])

            if encontrar_coincidencias(apellido, patron) == True:
                resultados[coincidencias] = i
                nuevo = [None] * (len(resultados) + 1)
                for j in range(len(resultados)):
                    nuevo[j] = resultados[j]
                resultados = nuevo
                coincidencias += 1
        retorno = True

        if coincidencias == 0:
            print("\nNo se encontraron participantes con ese apellido.")
            retorno = False

        if retorno == True:
            print("\nCoincidencias encontradas:")
            for c in range(coincidencias):
                pos = resultados[c]
                mostrar_calificacion(array_participantes, matriz_votos, pos )
        
        pregunta = input(f"Quiere buscar otro partido(S/N): ")
        if pregunta == "N" or pregunta == "n":
            retorno = True
        elif pregunta == "S" or pregunta == "s":
            retorno = False
        else:
            print("Error")
            
    return retorno



