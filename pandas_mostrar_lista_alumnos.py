import pandas as pd
import leer_datos_json


def imprimir_lista_alumnos():
    lista_alumnos = leer_datos_json.get_lista_alumnos()
    p1 = []
    p2 = []
    p3 = []
    promedio = []

    # Se asignan valores a las variables previamente declaradas. Los valores asignados a cada variable dependen de si el alumno en cuestion tiene o no las notas agregadas en el sistema.
    for alumno in lista_alumnos:
        # Si tiene notas registradas estas se asignan a las variables correspondientes
        if(alumno["notas"]): 
            p1.append(alumno["notas"][0])
            p2.append(alumno["notas"][1])
            p3.append(alumno["notas"][2])
            promedio.append(alumno["notas"][3])
        # Si NO tiene notas registradas se asignan guiones a las variables correspondientes
        elif(not alumno["notas"]):
            p1.append("-")
            p2.append("-")
            p3.append("-")
            promedio.append("-.-")

    # Se crea un nuevo DataFrame en base a los datos contenidos en el archivo json
    df = pd.read_json(r"datos-alumnos.json")
    del df['notas']  # Elimina la columna notas del DataFrame previamente creado

    # Agrega 3 columnas al DataFrame
    df.columns = ["CARNET", "NOMBRE", "APELLIDO"]

    # Llena las columnas con los datos contenidos en las variables p1, p2, p3 y promedio
    df["NOTA 1"] = p1
    df["NOTA 2"] = p2
    df["NOTA 3"] = p3
    df["PROMEDIO"] = promedio

    print()
    print(df) # Imprime el DataFrame en pantalla
    print()
