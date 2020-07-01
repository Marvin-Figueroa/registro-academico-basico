import pandas as pd
from validar_carnet import es_carnet_valido
import leer_datos_json
import buscar_alumno


def imprimir_alumno():
    while True:
        carnet = input("Ingrese el carnet del alumno a mostrar: ").upper()

        if(not es_carnet_valido(carnet)):
            print("Carnet Invalido - Respetar formato AB12345")
        elif(buscar_alumno.indice_alumno(carnet, leer_datos_json.get_lista_alumnos()) == -1):
            print("\nEl carnet ingresado no existe. Debe registrar al alumno.\nPuede registrarlo seleccionando la opcion en el menu.")
            # Regresar al menu principal
            return
        else:
            break

    indice = buscar_alumno.indice_alumno(
        carnet, leer_datos_json.get_lista_alumnos())
    alumno = leer_datos_json.get_lista_alumnos()[indice]

    columnas = ["CARNET", "NOMBRE", "APELLIDO",
                "NOTA 1", "NOTA 2", "NOTA 3", "PROMEDIO"]
    # Crea un nuevo DataFrame con las columnas previamente definidas
    df = pd.DataFrame(columns=columnas)

    # Verifica que el alumno tenga notas registradas en el sistema, si es asi se agregan a la columna correspondiente del DataFrame. Si no es asi, solo se agregan carnet, nombre y apellido y en las columnas de notas se agregan guiones.
    if(alumno["notas"]):

        df.loc[0] = [alumno["carnet"], alumno["nombre"], alumno["apellido"], alumno["notas"][0], alumno["notas"]
                     [1], alumno["notas"][2], alumno["notas"][3]]

    if(not alumno["notas"]):

        df.loc[0] = [alumno["carnet"], alumno["nombre"],
                     alumno["apellido"], "-", "-", "-", "-.-"]

    print()
    print(df)
    print()

    return
