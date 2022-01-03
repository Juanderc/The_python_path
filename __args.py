# *args como paramentro me ayuda a tomar n cantidad de parametros
def suma(*args):
    lista = list(args)
    string = " ".join(lista)

    return string.replace(" ", "-")


print(suma("I","love","Python","!"))


# **args como parametro me ayuda a tomar n parametros y crear diccionario
def datos(**args):
    print(args)


datos(nombre='Jose', apellido='Perez')



