#Operaciones de Entrada / Salida en Consola 
#El resultado de ingresar informacion por medio de input es un STRING
name = input("Ingrese su nombre: ")
#age = int(input("Ingrese su edad: ")) #Utilizamos int para transformar de un string a un int
age = float(input("Ingrese su edad: ")) #Utilizamos float para transformar de un string a un float
print(f"Mi nombre es {name} y mi edad es de {age} años")
print(type(name))
print(type(age))