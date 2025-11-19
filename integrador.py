libros = []

print("=== Carga de libros de la biblioteca ===")
print("Escriba 'fin' en el título para terminar.\n")

try:
    while True:
        titulo = input("Título del libro (o 'fin' para terminar): ")
        if titulo.lower().strip() == "fin":
            break

        autor = input("Autor: ")
        anio = input("Año de publicación: ")
        genero = input("Género: ")

        libro = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "genero": genero
        }

        libros.append(libro)

except Exception:
    print("Ocurrió un error durante la carga de datos.")

try:
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        for libro in libros:
            linea = f"{libro['titulo']};{libro['autor']};{libro['anio']};{libro['genero']}\n"
            f.write(linea)

    print("\nLos libros se guardaron correctamente en biblioteca.txt")

except Exception:
    print("Ocurrió un error al escribir el archivo.")


libros_leidos = []

try:
    with open("biblioteca.txt", "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(";")
            if len(datos) == 4:
                libro = {
                    "titulo": datos[0],
                    "autor": datos[1],
                    "anio": datos[2],
                    "genero": datos[3]
                }
                libros_leidos.append(libro)

except Exception:
    print("Ocurrió un error al leer el archivo.")


print("\n=== Libros registrados ===")
for libro in libros_leidos:
    print(
        f"Título: {libro['titulo']}, "
        f"Autor: {libro['autor']}, "
        f"Año: {libro['anio']}, "
        f"Género: {libro['genero']}"
    )
