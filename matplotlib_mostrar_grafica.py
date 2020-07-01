import matplotlib.pyplot as plt
import leer_datos_json


def generar_grafica():
    listado_alumnos = leer_datos_json.get_lista_alumnos()
    notas1 = []
    notas2 = []
    notas3 = []
    promedios = []
    carnets_alumno = []
    xpos = []
    alumno_actual = 0

    # Se asignan los valores a las variables previamente declaradas; los cuales serviran para generar la grafica (se incluyen los carnets, notas y promedios asociados a cada uno - solo si el alumno ya tiene las notas registradas)
    for alumno in listado_alumnos:
        if(alumno["notas"]):
            notas1.append(alumno["notas"][0])
            notas2.append(alumno["notas"][1])
            notas3.append(alumno["notas"][2])
            promedios.append(alumno["notas"][3])
            carnets_alumno.append(alumno["carnet"].upper())
            xpos.append(alumno_actual)
            alumno_actual += 1

    # Coloca las etiquetas con los carnets en el eje x (base de la grafica) con una rotacion de 25 grados de derecha hacia arriba
    plt.xticks(xpos, carnets_alumno, rotation=25)

    # Generan cada una de las 4 lineas con puntos que conforman la grafica
    plt.plot(xpos, notas1, color='#2980b9', linestyle='solid', linewidth=2,
             marker='o', markerfacecolor='#2980b9', markersize=3, label='Nota 1')

    plt.plot(xpos, notas2, color='#27ae60', linestyle='solid', linewidth=2,
             marker='o', markerfacecolor='#27ae60', markersize=3, label='Nota 2')

    plt.plot(xpos, notas3, color='#8e44ad', linestyle='solid', linewidth=2,
             marker='o', markerfacecolor='#8e44ad', markersize=3, label='Nota 3')

    plt.plot(xpos, promedios, color='#c0392b', linestyle='dotted', linewidth=2,
             marker='o', markerfacecolor='#c0392b', markersize=3, label='Promedio')

    # Modifica el rango de las etiquetas del eje y ( van de 0 a 10, de uno en uno, el 11 no se incluye en el rango)
    plt.yticks(range(0, 11, 1))

    # Cambia el tamaño de letra de las etiquetas de los ejes X-Y (ALUMNOS y CALIFICACIONES)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=10)

    # Coloca la etiqueta del eje X
    plt.xlabel('ALUMNOS')

    # Coloca la etiqueta del eje Y
    plt.ylabel('CALIFICACIONES')

    # Coloca el titulo de la grafica
    plt.title('CALIFICACIONES DE ALUMNOS CICLO I - 2020')

    # Indica que la leyenda (donde aparece el color asociado a cada linea y que representa cada linea en la grafica) esté presente.
    plt.legend()

    # Cambia el tamaño de letra y la posicion de la leyenda (loc=4 indica esquina inferior derecha para la posicion)
    plt.legend(loc=4, prop={'size': 6})

    # Muestra la grafica en pantalla
    plt.show()
