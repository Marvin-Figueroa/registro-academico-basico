import re # Importa el modulo "re" el cual sirve para trabajar con expresiones regulares en Python

# Se crea la expresion regular la cual indica que un nombre o un apellido valido es aquel que unicamente contiene entre 3 y 20 LETRAS del alfabeto.
nombreApellidoPattern = "^[a-zA-Z]{3,20}$"

# Verifica si el nombre o apellido recibido como parametro es valido comparandolo con la expresion regular anterior, retorna True si es asi y False si no
def es_nombre_apellido_valido(nombre_apellido):
    if(re.fullmatch(nombreApellidoPattern, nombre_apellido) is None):
        return False
    else:
        return True
