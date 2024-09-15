# Manejo de archivos .txt en Python

# 1. Leer un archivo línea por línea:
# Abrimos el archivo 'cuento.txt' en modo lectura ('r'). El ciclo for recorre cada línea.
# La función strip() elimina espacios en blanco y saltos de línea al principio y al final de cada línea.
with open('cuento.txt', 'r') as file:
    for cada_linea in file:
        print(cada_linea.strip())  # Quitamos espacios y saltos de línea innecesarios.

# 2. Leer todas las líneas en una lista:
# readlines() lee todas las líneas del archivo y las almacena en una lista donde cada línea es un elemento.
with open('cuento.txt', 'r') as file:
    lines = file.readlines()  # Guardamos todas las líneas del archivo como una lista.
    print(lines)

# 3. Añadir texto al final de un archivo (modo 'a'):
# Abrimos el archivo en modo append ('a'), lo que permite agregar contenido al final del archivo sin modificar lo existente.
with open('cuento.txt', 'a') as file:
    file.write("\n\nIn collaboration with Pacool84")  # Agregamos una nueva línea al final del archivo.

# 4. Sobrescribir el contenido de un archivo (modo 'w'):
# Modo escritura ('w'). Este modo reemplaza todo el contenido del archivo.
# ⚠️ ¡Precaución! Usar con cuidado ya que este proceso borra todo el contenido anterior.
with open('cuento.txt', 'w') as file:
    file.write("Hemos borrado el archivo")  # El contenido anterior se pierde y es reemplazado.