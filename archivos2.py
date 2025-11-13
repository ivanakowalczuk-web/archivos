from pathlib import Path

# Obtener la ruta actual
ruta = Path.cwd()
print("Directorio actual:", ruta)

# Crear una carpeta nueva si no existe
carpeta = ruta / "nueva_carpeta"
carpeta.mkdir(exist_ok=True)

# Crear un archivo dentro de la carpeta
archivo = carpeta / "ejemplo.txt"
archivo.write_text("Primera línea\nSegunda línea con acento: información\nTercera línea", encoding="utf-8")

# Leer el contenido completo
contenido = archivo.read_text(encoding="utf-8")
print("\nContenido del archivo:")
print(contenido)

# Leer línea por línea (manejo de posibles errores de codificación)
print("\nLíneas del archivo:")
with archivo.open("r", encoding="utf-8", errors="replace") as f:
    for linea in f:
        print(linea.strip())

# Mostrar información del archivo
print("\nInformación del archivo:")
print("Nombre:", archivo.name)
print("Sufijo:", archivo.suffix)
print("Tamaño:", archivo.stat().st_size, "bytes")
print("Existe:", archivo.exists())

# Renombrar el archivo
archivo_renombrado = carpeta / "archivo_final.txt"
archivo.rename(archivo_renombrado)
print("\nArchivo renombrado a:", archivo_renombrado.name)

#Eliminar el archivo y la carpeta
#archivo_renombrado.unlink()
#carpeta.rmdir()
#print("\nArchivo y carpeta eliminados correctamente.")

