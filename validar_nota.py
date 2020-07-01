# Verifica que la nota recibida como parametro sea un entero comprendido entre 0 y 10 y retorna un Boolean = True si es asi y False si no.
def esNotaValida(nota):
    try:
        nota = eval(nota)

        if (not (isinstance(nota, int) or (isinstance(nota, float)))):
            raise ValueError()

        if (nota < 0 or nota > 10):
            raise ValueError()

        return True

    except (NameError, ValueError, SyntaxError):
        return False
