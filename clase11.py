#Diccionarios son una estrucutra de datos que almacenan dos datos la "clave" y el "valor" "key/value"

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)
print(type(numbers))

#Accediendo a la informacion de los diccionarios
#Aqui mandamos llamar a la "clave" 

print(numbers[1])
print(numbers[2])
print(numbers[3])

person = {"nombre": "Sebastian",
          "apellido": "Lopez",
          "edad": 40}

print(person)
print(person["nombre"], person["apellido"], person["edad"])

#Eliminando informacion de un diccionario

del(person["edad"])
print(person)

#Metodos para trabajar con diccionarios
#KEYS, obtiene las claves del diccionario 

person2 = {"nombre": "Paco",
          "apellido": "Lopez",
          "edad": 40,
          "altura": 1.73}

claves = person2.keys()
print(claves)
print(type(claves))

#VALUES, obtiene los valores del dicccionario

valores = person2.values()
print(valores)
print(type(valores))

#ITEMS, obtiene la clave y el valor del diccionario

both_info = person2.items()
print(both_info)
print(type(both_info))

