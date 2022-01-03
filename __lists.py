
print("# ===================tuplas====================== \n")

"""
En ciertas ocasiones tendremos la necesidad de obtener algunos elementos de nuestras tuplas, por ejemplo, teniendo la siguiente tupla.

tupla = (10, 20, 30, 40, 50)

Necesito obtener el primero, el segundo y el último elemento; Para lograr esto tendremos un par de opciones; trabajando con índices y sin ellos. Veamos.

Si trabajamos con índices podemos hacerlo lo siguiente.

primero = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]

o simplemente podemos reducir las líneas de código y dejarlo en una sola.

primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]

La segunda opción es dejar de trabajar con las los índices y utilizar el guión bajo _.

primero, segundo, _, _, ultimo = tupla

Como observamos he colocado dos guiones bajos que hacen referencia a el número 30 y el número 40, valores que no necesitamos, por en de, no necesito almacenarlos en alguna variable; simplemente los ignoramos.

Ahora, que pasa si tengo una tupla mucho más grande y nuevamente necesito obtener esos tres elementos (el primero, el segundo y el último).

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

Lo que podemos hacer es utilizar el guión bajo _ junto con el asterisco * y aplicar lo que hemos visto anteriormente.

primero, segundo, *_, ultimo = tupla

De esta forma podemos trabajar de una forma más eficiente con las tuplas.
"""

lista = ("jose", "daniel", "pedro")
n_1, n_2, n_3 = lista  # Asigna un valor a cada variable

lista_2 = (3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals = lista_2

# Imprime todos los valores sobrantes de la Tupla
print(vals)

segundos = 5 * 31, 556, 926
print(segundos)

"""imprime una tupla con el resultado de la multiplicacion de 5 por 
cada numero separados con ',' """

print("# ===================listas====================== \n")


lista1 = ["jose", "daniel", "pedro", "maria", "daniela", "josefa"]

print(lista1[1])  # imprime el segundo elemento===
print(lista1[0:2])  # imprime los dos primeros
print(lista1[0:3:2])  # imprime del primero al 2 haciendo saltos
print(lista1[::-1])  # imprime la lista al reves

print("# ========================================== \n")

segundos = [5 * 31, 556, 926]
print(segundos)

print("# ========================================== \n")

segundos = [5 * 31, 556, 926]

# La funcion sort(reverse=True) imprime los valores en orden pero de reversa
segundos.sort(reverse=True)
print("Orden en reversa:", segundos)

# Imprime el minimo valor
print("Minimo", min(segundos))

# Imprime el maximo valor
print("Maximo:", max(segundos))

# Imprime la longitud de la lista
print("Longitud de la lista:", len(segundos))

""" Imprime un booleano True o False dependiendo de 
si se encuentra el numero en la lista """
print(8 in segundos)

# Imprime el indice del numero en lista
print("Indice de 155:", segundos.index(155))

# Imprime la cantidad de veces que encuentra un dato en lista
print("Cantidad de veces que aparece 155:", segundos.count(155))

# Inserta un elemento a la lista
nuevo_val = segundos.insert(2, 3)
print(nuevo_val)

""" Limpia una lista"""
# print(segundos.clear())

"""Remueve elementos de una lista"""
# print(segundos.remove())


"""imprime una lista con el resultado de la multiplicacion de 5 por 
cada numero separados con ',' """


"""
Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.

    [:] Todos los elementos.
    [start:] Todos los elementos desde el índice establecido(start).
    [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
    [start:end] Todos los elementos de un rango de índices.
    [start:end:step] Todos los elementos de un rango de índices con saltos.

    De igual forma, este listado es aplicable a las tuplas y los strings.

"""

"""
Comparacion de listas

sort()#ordena las listas para luego comparar

l1 = [10, 20, 30, 40, 50] 
l2 = [10, 20, 30, 50, 40, 70] 
l3 = [50, 10, 30, 20, 40] 
 
l1.sort() 
l2.sort() 
l3.sort() 
 
if l1 == l3: 
    print ("The lists l1 and l3 are the same") 
else: 
    print ("The lists l1 and l3 are not the same") 
 
 
if l1 == l2: 
    print ("The lists l1 and l2 are the same") 
else: 
    print ("The lists l1 and l2 are not the same") 


set()#compara dos listas sin importar el orden 

l1 = [10, 20, 30, 40, 50] 
l3 = [50, 10, 30, 20, 40] 
 
a = set(l1)
b = set(l3)
 
if a == b:
    print("Lists l1 and l3 are equal")
else:
    print("Lists l1 and l3 are not equal")

"""

"""
split is a function in Python that allows us to convert a string into 
a list with each word of the string

txt = "Hello wordl"
txt.split()

#By default split any white space is a separator


"""
print("# ===================Matriz======================= \n")


lista_1 = [32, 10]
lista_2 = [10, 40]

if 10 in lista_1:
    print("10 in list")

matriz = [lista_2, lista_1]
elemento = matriz[1][0]
print("Posicion de elemento en matriz:", elemento)


print("# ====================Lista y Tupla====================== \n")

lis = [1, 2, 3, 4]
tup = (5, 6, 7, 8)

valores = zip(lis, tup)
valores_li = list(valores)  # Convierte el zip a una lista de tuplas
valores_tu = tuple(valores)  # Convierte el zip a una tupla de tuplas
print(valores_li)
print(valores_tu)


to_lis = list(tup)
to_tup = tuple(lis)

print(to_lis)
print(to_tup)


def assign():
    asig = to_lis.append(9)
    print(asig)


assign()

print(tup + (9,))


# Method 	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list
