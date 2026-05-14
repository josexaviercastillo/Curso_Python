# Listas ---- las listas almacenan varios valores de cualquier tipo
# pueden recorrerce con el indice, es decir desde el 0 que sería 
# el primer elemento o el 1 quue seria el segundo elemento 
lista = ["pepe", "plomo", 29, True]
print(lista[0])  # Imprime "pepe"}

#Con eesto se modifican los registros de la lista |||||
lista[0] = "pablo"
print(lista)

# Tuplas ---- las tuplas son similares a las listas pero son inmutables
# una vez creadas no pueden modificarse
tupla = ("pepe", "plomo", 29, True)
print(tupla[1])  # Imprime "plomo"

# Conjuntos ---- los conjuntos son colecciones desordenadas de elementos únicos
# no permiten elementos duplicados  
# no se puede acceder a los elementos mediante un índice
conjunto = {"pepe", "plomo", 29, True}
print(conjunto)  # Imprime el conjunto (el orden puede variar)

# Diccionarios ---- los diccionarios almacenan pares clave-valor key:value
# permiten acceder a los valores mediante sus claves                
diccionario = {
    "nombre": "pepe", 
    "apellido": "plomo", 
    "edad": 29, 
    "soltero": True}  
print(diccionario["nombre"])  # Imprime "pepe"


