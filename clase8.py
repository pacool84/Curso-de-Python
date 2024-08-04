to_do = ["Ir a desayunar", "Comprar Herramienta", "Instalar Electrodomesticos","Ir a descansar"]
print(to_do)

numbers = [1,2,3,4,"cinco"]
print(numbers)
print(type(numbers))

mix = ["uno", 2,3.14,True,[1,2,3]]
print(mix)
print(type(mix))

#Acceder a valores especificos
print(len(mix))

#indexacion
print(mix[0])
print(mix[1])
print(mix[2])
print(mix[3])

#Slice, porciones de los datos
print(mix[0:3])
print(mix[:5])
print(mix[1:])
print(mix[::-1])

#Metodos para trabajar con listas 
#Aumentar/Agregar un elemento en la lista 
mix.append("Hello World")
print(mix)

mix.append([True, False, 10])
print(mix)

#Añadiendo un elemento a la lista EN UN LUGAR ESPECIFICO
#Metodo Insert

mix.insert(1,"Usando INSERT")
print(mix)

mix.insert(len(mix), "Final de la lista")
print(mix)


#Consultar la primera aparicion de un elemento en una lista 
#Metodo INDEX

print(mix.index(True))

#Consultar en una lista el numero mayor y menor
#Metodo MAX y MIN

more_numbers = [9, 34, 40,42,50, 83]
print(more_numbers)
print('El numero mayor es: ', max(more_numbers))
print('El numero menor es: ', min(more_numbers))

#Consultar el nombre mas largo y corto con uso de KEY en metodo MAX y MIN

names = ["Sebastian","Victoria","Paco"]
large_name = max(names, key=len)
short_name = min(names, key=len)
print(names)
print(large_name)
print(short_name)

#Eliminando elemento de una lista 
#Metodo DEL 

del(more_numbers[-1])
print(more_numbers)

del(names[-1])
print(names)

del(mix[1:6])
print(mix)