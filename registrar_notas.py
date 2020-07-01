import json
from validar_nota import esNotaValida
from validar_carnet import es_carnet_valido
import leer_datos_json
import buscar_alumno

primeraNota = 0
segundaNota = 0
terceraNota = 0
promedio = 0
carnet = ""
caracteres_decorativos = 60


def ingresar_notas():
    listado_alumnos = leer_datos_json.get_lista_alumnos()
    while True:
        carnet = input("Ingrese el carnet del alumno: ").upper()

        if(not es_carnet_valido(carnet)):
            print("\nCarnet Invalido - Respetar formato AB12345")
        elif(buscar_alumno.indice_alumno(carnet, listado_alumnos) == -1):
            print("\nEl carnet ingresado no existe. Debe registrar al alumno.\nPuede registrarlo seleccionando la opcion en el menu.")
            # Regresar al menu principal
            return
        elif(len(listado_alumnos[buscar_alumno.indice_alumno(carnet, listado_alumnos)]["notas"]) == 4):
            print("\nEl alumno " + carnet +
                  " ya tiene las notas registradas.\nPuede modificarlas seleccionando la opcion en el menu.")
            # Regresar al menu principal
            return
        else:
            break

    while True:
        primeraNota = input(carnet + " - Primera Nota: ")

        if (esNotaValida(primeraNota)):
            break
        else:
            print("Nota Invalida")

    while True:
        segundaNota = input(carnet + " - Segunda Nota: ")

        if (esNotaValida(segundaNota)):
            break
        else:
            print("Nota Invalida")

    while True:
        terceraNota = input(carnet + " - Tercera Nota: ")

        if (esNotaValida(terceraNota)):
            break
        else:
            print("Nota Invalida")

    promedio = (eval(primeraNota) + eval(segundaNota) + eval(terceraNota)) / 3
    promedio = round(promedio, 2)

    listado_alumnos[buscar_alumno.indice_alumno(carnet, listado_alumnos)]["notas"] = [eval(
        primeraNota), eval(segundaNota), eval(terceraNota), promedio]

    with open("datos-alumnos.json", "w") as salida:
        json.dump(listado_alumnos, salida)

    print("*" * caracteres_decorativos)
    print("Notas del alumno " + carnet + " registradas con exito.")
    # Regresar al menu principal
    return
