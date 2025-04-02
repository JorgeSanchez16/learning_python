#Forma de definir un Diccionario
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))
#Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par clave: valor
my_dict = {"nombre":"Jorge", "apellido":"Sanchez", "edad":22, "Lenguajes": {"python","html"}}
print(my_dict)
print(type(my_dict))
print(len(my_dict))#Tiene cuatro datos en formato clave: valor

print(my_dict["nombre"])#Nos facilita el acceso al valor a través de la clava

my_dict["nombre"] = "Pedro" #De esta forma cambiamos el valor a través de la clave
print(my_dict["nombre"])

my_dict["Color"] = "rojo" #Añadir una nueva clave: valor
print(my_dict)

del my_dict["Color"] #Como eliminar una clave: valor
print(my_dict)


print(my_dict.items())#Un listado de cada uno de los objetos

print(my_dict.keys())#Un litado de cada uno de las claves

print(my_dict.values())#Un listado de cada uno de los valores

#print(my_dict.items())



















