import os

def borrar_json_en_carpeta(carpeta):
    # Recorre todos los archivos y subcarpetas en la carpeta especificada
    for carpeta_raiz, subcarpetas, archivos in os.walk(carpeta):
        for archivo in archivos:
            # Si el archivo es un .json, lo elimina
            if archivo.endswith(".json"):
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                os.remove(ruta_archivo)
                print(f"Archivo eliminado: {ruta_archivo}")
    else:
        print(f'En la ruta: {ruta_carpeta}, no hay archivos que eliminar.')

# Especifica la ruta de la carpeta
ruta_carpeta = input('Ingrese la ruta a explorar para borrar los archivos ".json": ')
borrar_json_en_carpeta(ruta_carpeta)
