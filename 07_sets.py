#Formas de definir un set
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))#Inicialmente es un diccionario

my_other_set = {"Jorge", "Sánchez", 1.60, 35}
print(type(my_other_set))#Al introcuirle datos de esta forma se convierte en un set

print(len(my_other_set))

my_other_set.add("JSgonzalez")
print(my_other_set) #Un set no es una estructura oredenada

my_other_set.add("JSgonzalez")
print(my_other_set)#Un set no permite elementos repetidos

print("Jorge" in my_other_set)#Para saber si un elemento existe en el set
print("Jorges" in my_other_set)

my_other_set.remove("Jorge")#Remueve un elemento del set
print(my_other_set)

my_other_set.clear()# Elimina todos los elementos del set
print(len(my_other_set))
