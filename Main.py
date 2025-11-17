from Funciones import *
from Inputs import*
import os

bandera_nombre = True
bandera_calificacion = True
array_nombres = ["Mauro Penrar","Raul Pendra"]
matriz_calificacion = [
    [7,8,7],
    [9,9,10],
]

# array_nombres = crear_array(6, None)
# matriz_calificacion = crear_matriz(6, 3)


input("\nIngrese una tecla para continuar...\n")

while True:
    mostrar_menu()
    opcion = ingresar_entero("\nSu opcion: ","Reingrese opcion (1-9): ",1,9)
    if opcion == 1:
        if cargar_nombre(array_nombres) == True:
            print("¡Carga realizada con exito!")
            bandera_nombre = True
        else:
            print("Error al realizar la carga")
    elif opcion == 2:
        if cargar_calificaciones(matriz_calificacion) == True:
            print("¡Carga realizada con exito!")
            bandera_calificacion = True
        else:
            print("Error al realizar la carga")
    elif opcion == 3 and bandera_nombre == True and bandera_calificacion == True:
        if mostrar_calificaciones(array_nombres, matriz_calificacion) == False:
            print("Error al mostrar los resultados")
    elif opcion == 4 and bandera_nombre == True and bandera_calificacion == True:
        if mayor_a(array_nombres, matriz_calificacion, 4) == False:
            print("Error al mostrar los promedios")
    elif opcion == 5 and bandera_nombre == True and bandera_calificacion == True:
        if mayor_a(array_nombres, matriz_calificacion, 8) == False:
            print("Error al mostrar los promedios")
    elif opcion == 6 and bandera_nombre == True and bandera_calificacion == True:
        if mostrar_jurado_estricto(matriz_calificacion) == False:
            print("Error al mostrar los jurados")
    elif opcion == 7 and bandera_nombre == True and bandera_calificacion == True:
        if mostrar_ganador(array_nombres, matriz_calificacion) == False:
            print("Error al mostrar al ganador")
    elif opcion == 8 and bandera_nombre == True and bandera_calificacion == True:
        buscar_apellido(array_nombres, matriz_calificacion)
    elif opcion == 9:
        print("Saliendo...")
        break
    else:
        print(f"No se puede acceder a la opcion {opcion} porque no se cargaron los datos.")
    input("Toque cualquier boton para continuar...")
    os.system("cls")

