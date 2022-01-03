import math
from types import MethodType

# Inside the oop(Object Orientation Programming) we have some
# words to know, first we have the class that define the way
# which we empakage the datas

# Second we have the 'instance' that define the object assingnet
# to a class

# Third we have 'attributes' that define the variables inside
# a class, there are thwo types of attributes,the instance
# variable and the class variable

# The class variable can only be accesed calling the class then
# the variable

# Animals.variable_name

# The instance variable can only be accesed calling the instance
# object and then the variable

#dog = Animals()
# dog.variable_name

# Fourth we have the 'methods' that define the functions inside
# the classes, there are class methods,static methods and
# instance method


class Ropa():
    className = 'Ropa'  # variable de clase(class variable)

    def __init__(self, m, c):
        self.marca = m  # variable de instancia(instace variable)
        self.color = c

    def detalle(self):  # metodo(method)
        print(self.marca, "y", self.color)


r1 = Ropa("Calvin Klein", "Blanco")
r1.detalle()

print("Nombre de la clase {}" .format(r1.className))
# hasattr devuleve un boleano si el objeto cuenta con un atributo especificado
print("El objeto cuenta con el atributo marca? {}" .format(
    hasattr(r1, "marca")))


class Animales():
    animal = "canguro"


a1 = Animales()
# setattr establece o crea un parametro a un atributo de la clase
setattr(a1, 'animal', 'pinguino')
setattr(a1, 'edad', '11')

print("Nombre del animal: {}" .format(a1.animal))
print("Edad del animal: {}" .format(a1.edad))

# delattr elimina el atributo especificado de una clase

delattr(a1, 'edad')
# print(a1.edad)

# Herencia


class Aereos():
    def __init__(self, marca, modelo, fecha):
        self.marca = marca
        self.modelo = modelo
        self.fecha = fecha


class Helicopteros(Aereos):

    def info(self, tipo):
        self.tipo = tipo
        print("Aeronave {}, modelo {}, tipo {} y fecha {}" .format(
            self.marca, self.modelo, self.tipo, self.fecha))


h1 = Helicopteros("Apache", "ss23", "2014")
print(h1.info("guerra"))

# ---------------------------Herencia Multiple---------------------


class Animal():
    def nadar(self):
        print("nadar")

    def ladrar(self):
        print("ladrar")


class Anfibio():
    def auyar(self):
        print("aouhhh")


class Perry(Animal, Anfibio):
    def morder(self):
        print("Morder")
# -----------------------------Sobre escritura de metodos-----------------------------

    def ladrar(self):
        super().ladrar()  # me permite acceder a la funcion o metodo padre
        print("ladrando")


an1 = Perry()
an1.ladrar()


""" Si un metodo no esta en una de las clases que hereda 
entonces lo busca en la clase padre, buscando dentro de las
clases de izquierda a derecha"""


print(issubclass(Perry, Animal))

"""Este metodo lo que hace es tomar la subclase y la 
clase padre para verificar si realmente es subclase, 
devolviendo True o False, cual sea el caso."""

"""this method take the subclass and the class pather to 
verify if it is really a subclass 

if Perry is subclass of Animal it return True"""


print(dir(an1))
"""Me devuelve los metodos que puedo usar con el objeto"""
"""This return the methods to use with the object"""


# ----------------------Metodos-Magicos en las clases--------------------------------

class Persona():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Hola {}".format(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}"  # it return the name of the class

    def __str__(self):
        return "Hello {}".format(self.name)


p1 = Persona("Jose")
print(p1.__repr__())
print(p1.__str__())
print(p1)


# --------------Metodos-De-Clase-y-Estaticos en las clases--------------------------------

class Pastel():
    def __init__(self, ingredients, area):
        self.ingredients = ingredients
        self.area = area

    def __repr__(self):
        return "Pastel de {}, area {}" .format(self.ingredients, self.area)

    def area(self):  # instance method
        return self.area_pastel(self.area)

    @staticmethod  # static method
    def area_pastel(area):
        return area ** 2 * math.pi

    @staticmethod  # static method
    def Lista(ingredientes):
        return (ingredients)

    @classmethod  # class method
    def Pastel_Chocolate(cls):
        return cls(['flour', 'milk', 'chocolate'])

    @classmethod
    def Pastel_Vainilla(cls):
        return cls(['flour', 'milk', 'vanilla'])


p1 = Pastel(['flour', 'milk', 'vanilla'], 32)
print(p1.area_pastel(4))
print(p1)


# ---------------------polymorphism---------------------------------

"""Consiste en crear varias clases con los mismos atributos,
pudiendo realizarse si los aributos tienen diferentes valores"""

"""It consist in use many class with the same attributes,
allowed realize if the attributes has differents values
"""


# example

class Lion():
    def kind_animal(self):
        print("Wild Animal")

    def height(self):
        print("Big")


class Dog():
    def kind_animal(self):
        print("Animal domestico")

    def height(self):
        print("Small")


animal_1 = Lion()
animal_2 = Dog()

for a in (animal_1, animal_2):
    a.kind_animal()
    a.height()


# ----------------------Decorated-Classes--------------------


class Decorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the decorator')
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        # Retorna un método(funcion de clase) si se llama en una instancia
        return self if instance is None else MethodType(self, instance)


class Test():
    @Decorator
    def __init__(self):
        print("Inside the class decorated")


class Test2():
    @Decorator
    def __init__(self):
        print("Inside the other class")


a = Test()
b = Test_2()


# ----------------------__get__--method-------------------------
# It excute ones the instance(object) is called and take the
# attributes of the class

class Examples:

    def __get__(self, instance, objtype=None):
        return instance.name


class Names:
    e = Examples()

    def __init__(self, name):
        self.name = name


a = Names("Gonzalo")
print(a.e)
