import os
from pathlib import Path

# Borra la terminal en cada ejecucion:
os.system('cls')

# Identifica la ruta desde la cual se realizo la ejecucion
ruta_actual = Path(__file__).parent
# Carpeta a escanear:
dir_escanear = '__source__'
# Ruta actual + carpeta a escanear:
ruta_escanear = Path(ruta_actual/dir_escanear)

# Diccionario de extensiones:
archivos = {
    "documentos": (".doc", ".docx", ".pdf", ".txt", ".odt", ".md", ".rtf", ".tex"),
    "imagenes": (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".tiff", ".ico"),
    "audio": (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".wma"),
    "video": (".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm"),
    "presentaciones": (".pptx", ".ppt", ".ppsx", ".pps", ".pptm", ".ppsm", ".potx", ".pot", ".potm"),
    "codigo": (".py", ".html", ".css", ".js", ".json", ".xml", ".c", ".cpp", ".java", ".bat", ".php", ".rb", ".go", ".sql", ".ts"),
    "archivos_comprimidos": (".zip", ".rar", ".tar.gz", ".7z", ".tar", ".gz", ".bz2"),
    "datos": (".csv", ".xls", ".xlsx", ".ods", ".db", ".sqlite", ".sqlite3", ".jsonl"),
    "ejecutables": (".exe", ".msi", ".app", ".sh", ".bin"),
    "fuentes": (".ttf", ".otf", ".woff", ".woff2")
}

# Inicializando contador de archivos encontrados:
archivos_count = {categoria: 0 for categoria in archivos}
archivos_count['otros'] = 0


def es_carpeta_vacia(ruta_dir):
    """Verifica si la carpeta es vacia (True) o no (False). | arg: ruta de la carpeta"""
    carpeta = Path(ruta_dir)
    return carpeta.is_dir() and not any(carpeta.iterdir())


def mover_archivo(ruta_archivo: Path, nombre_carpeta: str) -> None:
    """Crea una carpeta en la ruta actual con el nombre dado como argumento (carpeta),
    y mueve el archivo dado en forma de ruta Path a dicha carpeta.\n
    args\n:
    archivo --> Ruta del archivo (Path)
    nombre_carpeta --> Nombre de la carpeta (str)
    """
    # Crea la ruta de la carpeta con el nombre dado como parametro
    ruta_carpeta = ruta_escanear / nombre_carpeta
    # Creando la carpeta si no existe
    Path(ruta_carpeta).mkdir(parents=True, exist_ok=True)

    # Moviendo el archivo
    origen = ruta_archivo
    destino = ruta_carpeta / ruta_archivo.name
    origen.replace(destino)


def escanear_directorio(ruta: Path):
    """Escanea el directorio desde el que se ejecuta y organiza los archivos por directorios:\n
    ['documentos', 'imagenes', 'audio', 'video', 'codigo', 'archivos_comprimidos', 'datos']"""

    # Iteramos sobre cada archivo para clasificarlo según su extensión
    for item in ruta.iterdir():
        if item.is_file():
            archivo = item  # Ahora item se llamara archivo, para mejor lectura del codigo
            extension_encontrada = False  # Marca si el archivo fue clasificado correctamente

            # Verificamos si la extensión del archivo coincide con alguna categoría
            for categoria, extensiones in archivos.items():
                if archivo.name.lower().endswith(extensiones):  # .lower() hace la comparación insensible a mayúsculas
                    # Movemos el archivo a la carpeta con el nombre de la categoria
                    mover_archivo(archivo, categoria)
                    extension_encontrada = True
                    archivos_count[categoria] += 1
                    break  # Detenemos la búsqueda una vez clasificado

            # Si no se encontró coincidencia, lo agregamos a la categoría 'otros'
            if not extension_encontrada:
                mover_archivo(archivo, 'otros')
                archivos_count['otros'] += 1
        else:
            # Si la carpeta no esta vacia:
            if not es_carpeta_vacia(item):
                # Si nombre de la carpeta coincide con los que define el script para organizar los archivos:
                if item.name in archivos.keys():
                    print(
                        f"\nAdvertencia: Probablemente ya organizo este directorio:\n{item}\nDe todas maneras se hara de nuevo.\n")
                    nuevo_nombre = "_temp_" + item.name
                    ruta_nuevo_nombre = Path(
                        "\\".join(item.parts[0:-1]) + "\\" + nuevo_nombre)
                    # Renombrando la carpeta:
                    os.rename(item, ruta_nuevo_nombre)
                    item = ruta_nuevo_nombre

                escanear_directorio(item)

                try:
                    # Elimina el directorio una vez se han movido todos sus archivos
                    item.rmdir()
                except Exception as e:
                    # Mostrara un error si el directorio que se intenta borrar no esta vacio:
                    print(f'\nError: {e}')
            else:
                # Marca carpetas vacias
                nuevo_nombre = "___" + item.name
                ruta_nuevo_nombre = Path(
                    "\\".join(item.parts[0:-1]) + "\\" + nuevo_nombre)
                # Renombrando la carpeta:
                os.rename(item, ruta_nuevo_nombre)


def mostrar_info(dict_archivos_count: dict):
    """Muestra un informe de los archivos que se encontraron y se movieron.
    Recibe el diccionario 'archivos_count', modificado luego de la ejecucion
    del escaneo principal.
    """
    # Mostrando los resultados
    print("\nEncontrados:\n")
    # Para cada categoria, contador del diccionario
    for k, v in dict_archivos_count.items():
        print(f"- {k}: {v}")
    print("----------------------------------------")
    # Calculando el total de archivos encontrados:
    suma = sum(dict_archivos_count.values())
    print(f"Total: {suma} archivos organizados.")
    print("----------------------------------------")


if __name__ == "__main__":
    print("========================================")
    print("      FILE-ORGANIZER by DannxDev      ")
    print("========================================")
    # Verificando si existe la carpeta clave para escanear
    if os.path.isdir(ruta_escanear):
        if not es_carpeta_vacia(ruta_escanear):

            # El script esta enfocado en directorios y archivos sin ordenamiento previo:
            print("\n--- ¡ADVERTENCIA! ---")
            print("Este script reorganizará sus archivos de forma irreversible.")
            print(
                "Se modificara cualquier organización previa sin posibilidad de recuperación.")
            print(
                "Asegúrese de que sus archivos no hayan sido organizados previamente antes de continuar.")

            # Pide confirmacion para continuar:
            confirmar_escaneo = input(
                "\n¿Esta seguro que desea continuar? (S/N): ").upper()
            print("\n----------------------------------------")

            if confirmar_escaneo == 'S':
                # Organiza el directorio
                escanear_directorio(ruta_escanear)
                # Muestra un informe de archivos organizados:
                mostrar_info(archivos_count)
                print("Completado: Sus archivos se han organizado exitosamente.")

            else:
                # Cancela el escaneo:
                print("\nCancelado: Se ha interrumpido la operacion.")
        else:
            mostrar_info(archivos_count)
            print(
                f"\nError: Carpeta '{dir_escanear}' vacia.\nMueva sus archivos a '{dir_escanear}' y vuelva a ejecutar este codigo.")

    else:
        # Si no encuentra la carpeta '__source__' (carpeta a escanear) la crea en el directorio de ejecucion.:
        crear_carpeta = ruta_escanear / dir_escanear
        Path(crear_carpeta).mkdir(parents=True, exist_ok=True)
        print(
            f"\nError: Carpeta '{dir_escanear}' no encontrada | Se ha creado.\nMueva sus archivos a '{dir_escanear}' y vuelva a ejecutar este codigo.")

    # Evita el cierre instantaneo de la consola.
    input("\nPresiona Enter para cerrar: ")
