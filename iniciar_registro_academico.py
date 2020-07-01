import sys
from validar_opcion_menu import es_opcion_valida
from registrar_alumno import registrar
from eliminar_alumno import eliminar
from registrar_notas import ingresar_notas
from modificar_notas import modificar_nota
from pandas_mostrar_lista_alumnos import imprimir_lista_alumnos
from pandas_mostrar_alumno import imprimir_alumno
from modificar_datos_alumno import editar_alumno
from matplotlib_mostrar_grafica import generar_grafica

caracteres_decorativos = 60
opcion = 0


def menu_principal():

    while True:
        print("*" * caracteres_decorativos)
        print("++++++++++  Bienvenido al Registro Academico  ++++++++++")
        print("*" * caracteres_decorativos)

        opcion = input(
            "Ingrese el numero de la opcion correspondiente:\n\n1-Registrar alumno\n2-Editar datos alumno\n3-Eliminar alumno\n4-Registrar notas\n5-Modificar notas\n6-Ver datos alumno\n7-Listar todos los alumnos\n8-Ver grafico de notas\n9-Salir\n")

        print("*" * caracteres_decorativos)

        # Verifica que lo ingresado en el menu por el usuario sea un numero entero entre 1 y 9
        if (es_opcion_valida(opcion, 1, 9)):
            opcion = eval(opcion)
            break

        print("Debe ingresar una opcion valida")

    if (opcion == 1):
        print("++++++++++  Nuevo Registro de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        registrar()
        menu_principal()

    if (opcion == 2):
        print("+++++++++  Modificacion de Datos de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        editar_alumno()
        menu_principal()

    if (opcion == 3):
        print("+++++++++  Eliminacion de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        eliminar()
        menu_principal()

    if (opcion == 4):
        print("++++++++++  Ingreso de Notas de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        ingresar_notas()
        menu_principal()

    if (opcion == 5):
        print("++++++++++  Modificacion de Notas de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        modificar_nota()
        menu_principal()

    if (opcion == 6):
        print("++++++++++  Visualizacion de Datos de Alumno  ++++++++++")
        print("*" * caracteres_decorativos)
        imprimir_alumno()
        menu_principal()

    if (opcion == 7):
        print("++++++++++  Listado de Alumnos Inscritos  ++++++++++")
        print("*" * caracteres_decorativos)
        imprimir_lista_alumnos()
        menu_principal()

    if (opcion == 8):
        print("++++++++++  Generando Grafica de Notas  ++++++++++")
        print("*" * caracteres_decorativos)
        print("Nota: los alumnos que no poseen notas registradas\nen el sistema NO apareceran en la grafica.")
        print("*" * caracteres_decorativos)
        generar_grafica()
        menu_principal()

    if (opcion == 9):
        print("Hasta Luego...")
        print("*" * caracteres_decorativos)
        sys.exit(0)


menu_principal()
