.endswith() : Método para comprobar si una cadena es texto termina con un sufijo especifico.

    if archivo.endswith(".json") : Se verifica si el archivo(archivo) termina con al extencion '.json'


.walk() : Genera nombres de archivos en un directorio de manera recursiva, recorre todos los directorios y subdirectorios, devolviendo una tupla con 3 valores para cada directorio que visita.

    carpeta_raiz: La ruta del directorio actual que se está explorando.
    subcarpetas: Una lista de los subdirectorios dentro de carpeta_raiz.
    archivos: Una lista de los archivos en carpeta_raiz.



    for carpeta_raiz, subcarpetas, archivos in os.walk(carpeta)

        os.walk(carpeta) : Recorre la carpeta y todas ssu subcarpetas.
        En cada itereción devuelve una tupla de tres elementos, la ruta actual(carpeta_raiz), las subcarpetas(subcarpetas) y los archivos en esa carpeta(archivos).


### Resumen

-- os.walk() : Recorre la carpeta principal y todas sus subcarpetas.

-- .endswith(".json") : Verofoca si cada archivo tiene la extensión '.json'

-- Si un archivo tiene la extensión '.json', se elimina con 'os.remove()'