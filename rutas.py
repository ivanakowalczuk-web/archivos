from pathlib import Path
import os

# Obtener la ruta actual
ruta_actual = Path.cwd()
print("Directorio actual:", ruta_actual)

# Crear una nueva carpeta dentro del directorio actual
nueva_ruta = ruta_actual / "nueva_carpeta"
nueva_ruta.mkdir(exist_ok=True)

# Cambiar el directorio de trabajo a la nueva carpeta
os.chdir(nueva_ruta)
print("Ahora estás en:", Path.cwd())

# Crear un archivo dentro del nuevo directorio
archivo = Path("saludo.txt")
archivo.write_text("Hola, estoy acá", encoding="utf-8")
# with open("saludo.txt", "w+", encoding="utf-8") as f:
#     f.write("Hola, estoy acá")
#     f.seek(0)  # vuelve al principio del archivo
#     contenido = f.read()

# print("Contenido del archivo:", contenido)

# Leer y mostrar el contenido del archivo para verificar
contenido = archivo.read_text(encoding="utf-8")
print("Contenido del archivo:", contenido)
