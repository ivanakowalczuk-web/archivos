file = open("datos.txt", "w+", encoding="utf-8")  #Abre para escritura y lectura. Crea el archivo si no existe
file.write("Línea 1: Hola Mundo\n") #Escribe una línea en el archivo
file.write("Línea 2: Esta es una prueba.\n") #Escribe otra línea
file.write("Línea 3: ¡Adiós!\n") #Escribe una tercera línea
file.seek(0) #Mueve el cursor al inicio del archivo para leer desde el principio
contenido = file.read()  #Lee todo el contenido del archivo
print(contenido) #Imprime el contenido leído
file.close() #Cierra el archivo para liberar recursos

with open("datos.txt", "a+", encoding="utf-8") as file:
    file.write("Primera línea agregada\nSegunda línea agregada\n")
    file.seek(0)  # 🔁 Volver al inicio
    print("Posición del cursor:", file.tell())
    contenido = file.read()
    print("Contenido completo:\n", contenido)

file = open("datos.txt", "r+", encoding="utf-8")  # Abre para lectura y escritura el archivo ya debe existir
file.seek(0,2)
file.writelines(['Agregué otra línea más.\n', 'Y una línea final.\n'])
file.seek(0)
contenido = file.read()
file.close()
print("Contenido final del archivo:\n", contenido)

with open("datos.txt", "r", encoding="utf-8") as f:
    print("Contenido:\n", f.read())
    f.seek(0)             # vuelve al inicio del archivo
    print(f.readline())   # lee una línea
    f.seek(0)             # vuelve al inicio otra vez
    print(f.readlines())  # devuelve una lista con todas las líneas
