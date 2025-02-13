my_variable = "My String Variable"
my_int_variable = 4

#****************Algunas funciones del sistema***************
print(len(my_variable)) #para saber la longitud 

print("Mi edad es:", my_int_variable) #Concatenar

#Variables en una sola linea, Tener cuidado al utilizar esta sintaxis!s
name, surname, alias, age = "Jorge", "Sanchez", "JSgonzalez", 35
print("Me llamo", name, surname,"mi edad es", age, "mi alias es", alias)


first_name = input('Cuál es tu nombre: ') #input para introducir datos de la parte del cliente
age = input('Cuál es tu edad: ')

print(first_name)
print(age)

#Cambiamos el tipo y el valor
first_name = 10
age = "Loco"
print(first_name)
print(age)
print(type(first_name))
print(type(age))