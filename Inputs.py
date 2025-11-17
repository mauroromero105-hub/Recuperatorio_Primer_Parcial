from Funciones import*

def ingresar_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    valido = False
    while not valido:
        entrada = input(mensaje)

        if len(entrada) == 0:
            valido = False
        else:
            valido = True
            for auxiliar in entrada:
                if auxiliar < '0' or auxiliar > '9':
                    valido = False
                    break

        if not valido:
            print("Error: debe ingresar solo números enteros.")
            continue

        numero = 0
        for auxiliar in entrada:
            numero = numero * 10 + (ord(auxiliar) - 48)
        
        if numero < minimo or numero > maximo:
            print(mensaje_error)
            valido = False
    return numero

def validar_caracteres(cadena:str, minimo: int) -> bool:
    bandera = True
    for auxiliar in cadena:
        codigo = ord(auxiliar)
        if not ((codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)):
                bandera = False
                break
    
    if len(cadena) < minimo:
        bandera = False
    
    return bandera

def validar_numero(voto: str, minimo: int, maximo: int) -> bool:
    bandera = True

    for i in range(len(voto)):
        codigo = ord(voto[i])
        if not (48 <= codigo <= 57): 
            bandera = False
            break

    if not bandera or len(voto) == 0:
        bandera = False

    numero = 0
    for i in range(len(voto)):
        numero = numero * 10 + (ord(voto[i]) - 48)

    if numero < minimo or numero > maximo:
        bandera = False

    return bandera

def ingresar_nombre_apellido(mensaje_nombre: str, mensaje_apellido: str, mensaje_error: str, cantidad_minima: int) -> str:
    bandera = False
    cadena_nueva = ""
    while not bandera:
        nombre = input(mensaje_nombre)

        if validar_caracteres(nombre, cantidad_minima):
            bandera = True
            cadena_nueva += nombre
            cadena_nueva += " "
        else:
            print(mensaje_error)

    bandera2 = False
    while not bandera2:
        apellido = input(mensaje_apellido)
        if validar_caracteres(apellido, cantidad_minima):
            bandera2 = True
            cadena_nueva += apellido
        else:
            print(mensaje_error)

    return cadena_nueva

def ingresar_votacion(mensaje_votacion: str, mensaje_error: str, cantidad_minima: int, cantidad_maxima:int) -> int:
    bandera = False

    while not bandera:
        voto = input(mensaje_votacion)

        if validar_numero(voto, cantidad_minima, cantidad_maxima):
            
            numero = 0
            for i in range(len(voto)):
                numero = numero * 10 + (ord(voto[i]) - 48)
                bandera = True
        else:
            print(mensaje_error)
    
    return numero

def cargar_nombre(array_nombre: list) -> bool:
    if type(array_nombre) == list and len(array_nombre) > 0:
        retorno = True
        for i in range(len(array_nombre)):
            print(f"Ingrese el participante {i + 1}")
            nombre_apellido = ingresar_nombre_apellido("Ingresar su primer nombre: ", "Ingresar su apellido: ", "Error, caracter incorrecto/insuficiente (Solo letra/Sin espacios)", 3)
            array_nombre[i] = nombre_apellido
    else:
        retorno = False
    
    return retorno

def cargar_calificaciones(matriz: list):
    retorno = False
    
    if type(matriz) == list and len(matriz) > 0:    
        for fila in range(len(matriz)):
            if type(matriz[fila]) == list:
                print(f"\n--- Ingreso de votos para el participante {fila + 1} ---")
                for col in range(len(matriz[fila])):
                    voto = ingresar_votacion(f"Ingrese el voto del jurado {col + 1} (0 a 10): ","Número/caracter no permitido", 0, 10)
                    matriz[fila][col] = voto
                    retorno = True
    else: retorno = False

    return retorno
