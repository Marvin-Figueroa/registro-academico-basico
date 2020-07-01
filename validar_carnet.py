import re #importa el modulo para trabajar con expresiones regulares en python

# Se crea la expresion regular la cual indica que un carnet valido es aquel que comienza con exactamente 2 LETRAS del alfabeto y termina con exactamente 5 numeros cualquiera del 0 al 9.
carnetPattern = "^[a-zA-Z]{2}[0-9]{5}$"

# Verifica si el carnet recibido como parametro es valido comparandolo con la expresion regular anterior, retorna True si es asi y False si no
def es_carnet_valido(carnet):
    if(re.fullmatch(carnetPattern, carnet) is None):
        return False
    else:
        return True
