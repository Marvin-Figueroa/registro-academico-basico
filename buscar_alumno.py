# Busca el carnet del alumno en la List(listado_alumnos) de Dicts(alumno).
# Para hacer que la comparacion entre carnets de alumnos sea caseInsensitive, ambos se pasan a mayuscula antes de compararlos.
# Si se encuentra una coincidencia se retorna el indice/posicion del alumno dentro de la List; en caso contrario se retorna -1

def indice_alumno(carnet, listado_alumnos):
    for alumno in listado_alumnos:
        if(alumno["carnet"].upper() == carnet.upper()):
            return listado_alumnos.index(alumno)
    return -1
