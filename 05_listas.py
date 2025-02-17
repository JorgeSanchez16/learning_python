#*************Listas******************
#Formas posibles de declarar una lista
my_list = list() 
my_other_list = []


my_list = [22, 35, 24, 30, 30, 17]
print(my_list) #Imprimo los datos de mi lista
print(len(my_list)) #Imprimo la longitud de mi lista

my_other_list = [22, 1, 22, "Jorge", "JS"]# Las listas pueden tener varios tipo de datos
print(type(my_other_list))# El tipo de dato es list
print(my_other_list) 

#Podemos utilizar las posiciones de forma independiente
#Las listas comienzan en la posición 0
print(my_list[0])
print(type(my_other_list[0]))#El dato es de tipo int en la posición 0
print(type(my_other_list[3]))#El dato es de tipo str en la posición 0
print(my_other_list.count(22))#Retorna el número de ocurrencias de un valor


print(my_list + my_other_list)#Concatenar dos listas

my_other_list.append("JSgonzalez")#Para añadir un elemento al final de la lista
print(my_other_list)

my_other_list.insert(3, "Azul")#Insertar un elemento en la posición que tu quieras
print(my_other_list)

my_other_list.remove("Azul")#Para remover un elemento de la lista
print(my_other_list)

my_other_list.pop(2)#Para remover un elemento, por defecto sera el último y devuelve el elemento que eliminamos
print(my_other_list)


del my_other_list[2]#Para remover el elemento de la posición que yo quiera
print(my_other_list)


my_new_list = my_list.copy()#Para copiar los datos de una lisa 
my_list.clear()#Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()#Para invertir el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort()#Para enviar criterios para ordenar la lista
print(my_new_list)