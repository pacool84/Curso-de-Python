a = [9,34,40,42,83]
b = a #Esta igualdad hace referencia a la informacion pero tambien al MISMO ESPACIO EN MEMORIA, por lo que cualquier modificacion en "a" tambien se reflejara en "b"
print(a)
print(b)

del(a[1])#Lo que borramos en a, tambien se borra en b
print(a)
print(b)

#PRO TIP
#Saber a que espacio en memoria apuntan la variables 
print("El espacio en memoria de a es: ",id(a))
print("El espacio en memoria de b es: ",id(b))

#Para poder evitar lo anterior podemos usar el metodo slice 
#Este metodo puede hacer una copia de la informacion en la lista y apunta a un espacio en memoria diferente

c = a[:]
print("El espacio en memoria de a es: ", id(a), a)
print("El espacio en memoria de b es: ", id(b), b)
print("El espacio en memoria de c es: ", id(c), c)

#Modificando a para validar que c no se modifique 

a.append(True)
print("Los valores de a son: ",a)
print("Los valores de b son: ",b)
print("Los valores de c son: ",c)
