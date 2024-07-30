name = "Paco"
print(type(name))

#Otras formas para definir variables de tipo string

name_2 = 'Sebas'
print(type(name_2))

name_3 = '''Brenda'''
print(type(name_3))

#Indexacion en los strings 

indexingString = "Hola mi amigo Python"
print(indexingString[14])

#Acceder a la ultima posicion de un string

indexingString = "Sebastian"
print(indexingString[-1])
print(indexingString[-2])

#Concatenacion de strings 
name = 'Carla Marcela'
last_name = 'Florida Roman'
print(name + ' ' + last_name)

#Repeticion de Strings 

new_name = 'Sebastian'
print(5 * new_name)

#Acciones sobre cadenas de texto, "length" longitud de la cadena o numero de caracteres en la cadena 

print(len(new_name))

#Metodos que se ejecutan en strings
#Pasar a minisculas o mayusculas 

other_name = 'VICTORIA'
another_name = 'sebastian'
print(other_name.lower())
print(another_name.upper())

#Remover espacios al principio y final de una cadena de texto

spaces_beginning_end = "      Sebastian y Brenda        "
print(spaces_beginning_end.strip())


