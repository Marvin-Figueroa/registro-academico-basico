import json
from validar_carnet import es_carnet_valido
import leer_datos_json
import buscar_alumno


caracteres_decorativos = 60


def eliminar():
    # Carga en memoria en la variable listado_alumnos todo el contenido del archivo json donde se guardan los datos del programa.
    listado_alumnos = leer_datos_json.get_lista_alumnos()

    while True:
        carnet = input("Ingrese el carnet del alumno a eliminar: ").upper()

        if(not es_carnet_valido(carnet)):
            print("Carnet Invalido - Respetar formato AB12345")
        elif(buscar_alumno.indice_alumno(carnet, listado_alumnos) == -1):
            print("\nEl carnet ingresado no existe. Debe registrar al alumno.\nPuede registrarlo seleccionando la opcion en el menu.")
            return  # Regresar al menu principal
        else:
            break
    # Elimina de la List de Dicts alumno el alumno ubicado en la posicion devuelta por la funcion indice_alumno
    listado_alumnos.pop(buscar_alumno.indice_alumno(carnet, listado_alumnos))

    # Abre el archivo json donde se guardan los datos del programa, en modo de escritura(w) y lo sobreescribe con los datos de la List actual donde ya se elimino el alumno.
    with open("datos-alumnos.json", "w") as salida:
        json.dump(listado_alumnos, salida)

    print("*" * caracteres_decorativos)
    print("Alumno eliminado con exito.")
    return
