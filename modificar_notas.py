import json
import leer_datos_json
from buscar_alumno import indice_alumno
from validar_carnet import es_carnet_valido
from registrar_notas import esNotaValida
from validar_opcion_menu import es_opcion_valida


opcion = 0
nueva_nota = -1
carnet = ""
caracteres_decorativos = 60


def actualizar_promedio(carnet, listado_alumnos):
    total_notas = 0
    for nota in range(3):
        total_notas = total_notas + listado_alumnos[indice_alumno(
            carnet, listado_alumnos)]["notas"][nota]

    # Se actualiza el promedio del alumno redondeando el valor a 2 decimales
    listado_alumnos[indice_alumno(carnet, listado_alumnos)]["notas"][3] = round(
        (total_notas / 3), 2)


def modificar_nota():
    # Carga en memoria en la variable listado_alumnos todo el contenido del archivo json donde se guardan los datos del programa.
    lista_alumnos = leer_datos_json.get_lista_alumnos()
    while True:
        carnet = input("Ingrese el carnet del alumno a modificar: ").upper()

        if(not es_carnet_valido(carnet)):
            print("Carnet Invalido - Respetar formato AB12345")
        elif(indice_alumno(carnet, lista_alumnos) == -1):
            print("\nEl carnet ingresado no existe. Debe registrar al alumno.\nPuede registrarlo seleccionando la opcion en el menu.")
            # Regresar al menu principal
            return
        elif(len(lista_alumnos[indice_alumno(carnet, lista_alumnos)]["notas"]) == 0):
            print("\nEl alumno " + carnet +
                  " no tiene notas registradas.\nPuede registrarlas seleccionando la opcion en el menu.")
            # Regresar al menu principal
            return
        else:
            break

    pos_alumno = indice_alumno(carnet, lista_alumnos)
    while True:
        opcion = input("\n" +
                       carnet + " - Seleccione la nota a modificar:\n\n1-Primera Nota\n2-Segunda Nota\n3-Tercera Nota\n4-Menu Principal\n")

        print("*" * caracteres_decorativos)

        if(es_opcion_valida(opcion, 1, 4)):
            opcion = eval(opcion)
            break
        else:
            print("Seleccione una opcion valida")
            print("*" * caracteres_decorativos)

    if (opcion == 1):
        while True:
            nueva_nota = input(carnet + " - Nota Actual: " + str(lista_alumnos
                                                                 [pos_alumno]["notas"][0]) + "\n" + carnet + " - Nueva Nota: ")

            if(esNotaValida(nueva_nota)):
                break
            else:
                print("Nota Invalida")

        lista_alumnos[pos_alumno]["notas"][0] = eval(nueva_nota)
        nueva_nota = -1

        actualizar_promedio(carnet, lista_alumnos)

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico la nota 1 y el promedio del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Nota 1 modificada con exito.")
        return

    if (opcion == 2):
        while True:
            nueva_nota = input(carnet + " - Nota Actual: " + str(lista_alumnos
                                                                 [pos_alumno]["notas"][1]) + "\n" + carnet + " - Nueva Nota: ")

            if(esNotaValida(nueva_nota)):
                break
            else:
                print("Nota Invalida")

        lista_alumnos[pos_alumno]["notas"][1] = eval(nueva_nota)
        nueva_nota = -1

        actualizar_promedio(carnet, lista_alumnos)

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico la nota 2 y el promedio del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Nota 2 modificada con exito.")
        return

    if (opcion == 3):
        while True:
            nueva_nota = input(carnet + " - Nota Actual: " +
                               str(lista_alumnos[pos_alumno]["notas"][2]) + "\n" + carnet + " - Nueva Nota: ")

            if(esNotaValida(nueva_nota)):
                break
            else:
                print("Nota Invalida")

        lista_alumnos[pos_alumno]["notas"][2] = eval(nueva_nota)

        actualizar_promedio(carnet, lista_alumnos)

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico la nota 3 y el promedio del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Nota 3 modificada con exito.")
        return

    if (opcion == 4):
        # Regresar al menu principal
        return
