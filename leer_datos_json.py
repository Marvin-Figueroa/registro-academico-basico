import json

#Abre en modo lectura(r) el archivo json donde se guardan todos los datos que maneja el programa("datos-alumnos.json"), lo lee y guarda el contenido en formato string en la variable string_data, cierra el flujo y finalmente convierte el string leido a una List de Dicts y la retorna.
def get_lista_alumnos():
    f = open("datos-alumnos.json", "r")
    string_data = f.read()
    f.close()
    return json.loads(string_data)
