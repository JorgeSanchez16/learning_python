#Formas de definir una Tuples
my_tuples = tuple()
my_other_tuples = ()

my_tuples = (22, 1.60, "Jorge", "JSgonzalez")
print(my_tuples)
print(type(my_tuples))


print(my_tuples[0]) 
print(my_tuples[-1])

print(my_tuples.count(22))#Retorna el número de ocurrencias de un valor
print(my_tuples.index("Jorge"))#Indica el índice del dato

#la principal diferencia de las tuplas con las listas es que son inmutables 