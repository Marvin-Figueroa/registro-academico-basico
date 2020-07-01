
# Verifica que la opcion recibida como parametro sea un entero comprendido entre "opcion_menor" y "opcion_mayor" y retorna un Boolean=True si es asi, y False si no.
def es_opcion_valida(opcion, opcion_menor, opcion_mayor):
    try:
        opcion = eval(opcion)

        if (not isinstance(opcion, int)):
            raise ValueError()

        if (opcion < opcion_menor or opcion > opcion_mayor):
            raise ValueError()

        return True
    except (NameError, ValueError, SyntaxError):
        return False
