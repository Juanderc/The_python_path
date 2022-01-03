print("#================Strings=========================")

texto = "Jose; Daniel; Pedro; Maria; Josefa;"

# El metodo split toma el caracter por el cual debe empezar a separar el string
resultado = texto.split("; ")
print(resultado)


# El metodo join toma el caracter por el cual debe empezar a separar la lista
resultado2 = "_".join(resultado)
print(resultado2)


text = """El metodo splitlines  
separara
el string que 
tiene saltos de 
linea"""
resultado3 = text.splitlines()
print(resultado3)

print("#================Strings-Con-Formato=========================")

text1 = "Python is easy"
result1 = text1.capitalize()
print(result1)


text2 = "Python is easy"
result2 = text2.upper()
print(result2)

text3 = "Python is easy"
result3 = text3.lower()
print(result3)

text4 = "Python is easy, Python is easy"
result4 = text4.replace("Python", "Nothing", 1)
print(result4)

text5 = "Python is easy"
result5 = "p" + text5[1:]
print(result5)


print("#================Strings-Con-Parametros=======================")


st = "Python is the best lenguage"
resul = "is" in st
print("The word 'is' in st:", resul)


st2 = "Python is the best lenguage"
resul2 = st2.count("best")
print("The word 'best' in st2:", resul2, "times")


st3 = "Python is the best lenguage"
resul3 = st3.find("lenguage")
print("The word 'lenguage' are on index:", resul3)


st4 = "Python is the best lenguage"
resul4 = st4.find("lenguage")
resul4 = st4[resul4:resul4 + len("language")]
print(resul4)

# Si el metodo find no encuentra el texto devuelve -1

st5 = "Python is the best lenguage"
resul5 = st5.startswith("Python")
print(resul5)


st5 = "Python is the best lenguage"
resul5 = st5.endswith("Python")
print(resul5)


print("===============Formatos-Strings==========================\n")

saludo = "Bienvenido"

print("{} Manuel".format(saludo))

print(f'{saludo} Manuel')

print("% s Manuel" % (saludo))
