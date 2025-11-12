from pathlib import Path

# Obtener la ruta actual
ruta = Path.cwd()
print("Directorio actual:", ruta)

try:
    # Crear una carpeta nueva si no existe
    carpeta = ruta / "nueva_carpeta"
    carpeta.mkdir(exist_ok=True)
    print(f"✅ Carpeta creada o existente: {carpeta}")

    # Crear un archivo dentro de la carpeta
    archivo = carpeta / "ejemplo.txt"

    # Escribir solo si no existe
    if not archivo.exists():
        archivo.write_text(
            "Primera línea\nSegunda línea con acento: información\nTercera línea",
            encoding="utf-8"
        )
        print(f"✅ Archivo creado: {archivo}")
    else:
        print(f"⚠️ El archivo ya existe: {archivo}")

    # Leer el contenido completo
    contenido = archivo.read_text(encoding="utf-8")
    print("\nContenido del archivo:")
    print(contenido)

    # Leer línea por línea
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

    # Renombrar el archivo (solo si no existe el destino)
    archivo_renombrado = carpeta / "archivo_final.txt"
    if not archivo_renombrado.exists():
        archivo.rename(archivo_renombrado)
        print("\n✅ Archivo renombrado a:", archivo_renombrado.name)
    else:
        print("\n⚠️ No se renombró: el archivo de destino ya existe.")

except FileExistsError as e:
    print("❌ Error: el archivo o carpeta ya existe ->", e)
except PermissionError as e:
    print("❌ Error de permisos ->", e)
except OSError as e:
    print("❌ Error del sistema de archivos ->", e)
except Exception as e:
    print("❌ Error inesperado ->", e)

# Limpieza opcional
try:
    if 'archivo_renombrado' in locals() and archivo_renombrado.exists():
        archivo_renombrado.unlink()
        carpeta.rmdir()
        print("\n🧹 Limpieza: archivo y carpeta eliminados.")
except Exception as e:
    print("⚠️ No se pudo limpiar completamente ->", e)
