import json
import leer_datos_json
from buscar_alumno import indice_alumno
from validar_carnet import es_carnet_valido
from validar_opcion_menu import es_opcion_valida
from validar_nombre_apellido import es_nombre_apellido_valido

opcion = 0
carnet = ""
caracteres_decorativos = 60


def editar_alumno():
    # Carga en memoria en la variable listado_alumnos todo el contenido del archivo json donde se guardan los datos del programa.
    lista_alumnos = leer_datos_json.get_lista_alumnos()
    while True:
        carnet = input("Ingrese el carnet del alumno a editar: ").upper()

        if(not es_carnet_valido(carnet)):
            print("Carnet Invalido - Respetar formato AB12345")
        elif(indice_alumno(carnet, lista_alumnos) == -1):
            print("\nEl carnet ingresado no existe. Debe registrar al alumno.\nPuede registrarlo seleccionando la opcion en el menu.")
            # Regresa al menu principal
            return
        else:
            break

    pos_alumno = indice_alumno(carnet, lista_alumnos)
    while True:
        opcion = input("\n" +
                       carnet + " - Seleccione el dato a modificar:\n\n1-Carnet\n2-Nombre\n3-Apellido\n4-Menu Principal\n")

        print("*" * caracteres_decorativos)

        if(es_opcion_valida(opcion, 1, 4)):
            opcion = eval(opcion)
            break
        else:
            print("Seleccione una opcion valida")
            print("*" * caracteres_decorativos)

    if (opcion == 1):
        while True:
            nuevo_carnet = input(
                "Carnet Actual: " + lista_alumnos[pos_alumno]["carnet"] + "\nCarnet Nuevo: ")

            if(es_carnet_valido(nuevo_carnet)):
                if(indice_alumno(nuevo_carnet, lista_alumnos) != -1):
                    print(
                        "\nEl carnet ingresado ya existe.\nEl nuevo carnet debe ser ¡¡¡NUEVO!!!")
                else:
                    break
            else:
                print("El nuevo carnet no es valido")

        lista_alumnos[pos_alumno]["carnet"] = nuevo_carnet.upper()

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico el carnet del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Carnet modificado con exito.")
        return

    if (opcion == 2):
        while True:
            nuevo_nombre = input(
                "Nombre Actual: " + lista_alumnos[pos_alumno]["nombre"] + "\nNuevo Nombre: ")

            if(es_nombre_apellido_valido(nuevo_nombre)):
                break
            else:
                print("El nuevo nombre no es valido")

        lista_alumnos[pos_alumno]["nombre"] = nuevo_nombre

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico el nombre del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Nombre modificado con exito.")
        return

    if (opcion == 3):
        while True:
            nuevo_apellido = input(
                "Apellido Actual: " + lista_alumnos[pos_alumno]["apellido"] + "\nNuevo Apellido: ")

            if(es_nombre_apellido_valido(nuevo_apellido)):
                break
            else:
                print("El nuevo apellido no es valido")

        lista_alumnos[pos_alumno]["apellido"] = nuevo_apellido

        # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se modifico el apellido del alumno.
        with open("datos-alumnos.json", "w") as salida:
            json.dump(lista_alumnos, salida)

        print("*" * caracteres_decorativos)
        print("Apellido modificado con exito.")
        return

    if (opcion == 4):
        # Regresar al menu principal
        return
