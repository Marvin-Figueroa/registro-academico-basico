import json
from buscar_alumno import indice_alumno
import leer_datos_json
from validar_carnet import es_carnet_valido
from validar_nombre_apellido import es_nombre_apellido_valido

carnet = ""
nombre = ""
apellido = ""
caracteres_decorativos = 60


def registrar():
    listado_alumnos = leer_datos_json.get_lista_alumnos()
    while True:
        carnet = input("Carnet: ").upper()
        if(not es_carnet_valido(carnet)):
            print("Carnet Invalido - Respetar formato AB12345")
        elif(indice_alumno(carnet, listado_alumnos) != -1):
            print("El carnet ingresado ya existe")
        else:
            break

    while True:
        nombre = input(carnet + " - Nombre: ")
        if(not es_nombre_apellido_valido(nombre)):
            print("Nombre Invalido - Debe ser solo un nombre sin espacios.")
        else:
            break

    while True:
        apellido = input(carnet + " - Apellido: ")
        if(not es_nombre_apellido_valido(apellido)):
            print("Apellido Invalido - Debe ser solo un apellido sin espacios.")
        else:
            break

    nuevo_alumno = {
        "carnet": carnet.upper(),
        "nombre": nombre,
        "apellido": apellido,
        "notas": []
    }

    listado_alumnos.append(nuevo_alumno)

    with open("datos-alumnos.json", "w") as salida:
        json.dump(listado_alumnos, salida)

    print("*" * caracteres_decorativos)
    print("Alumno registrado con exito")

    return
