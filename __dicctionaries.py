# Dictionaries

from collections import ChainMap
from types import MappingProxyType

dic = {}

dic["nombre"] = "Manuel"
dic["Edad"] = 19

# return the dictionary
print(dic)

# return a boolean
print("nombre" in dic)

# return the value
print(dic.get("Edad"))

# return a response if the key isnt defined
# it can return whatever data type boolean,string,dic,list,int,float,etc.
print(dic.get("dir", "No se encuentra la llave"))

# it put a value in a key, and if, its not defined, it create the key and put the value
print(dic.setdefault("dir", ()))

print(dic)

# return the keys of the dic
dic_key = dic.keys()
print(dic_key)

# it convert the keys
print(list(dic_key))
print(tuple(dic_key))


# return the values of the dic
print(dic.values())

# it delete a key and value
del dic["dir"]
# dic.pop("dir")

print(dic)

# it clean the dictionary
dic.clear()
print(dic)

# Use a dictionary in read-only mode
writable_mode = {"first": 1, "second": 1}
read_mode = MappingProxyType(writable_mode)
print(read_mode)
# error = read_mode["tirst"] = 3
# print(error)

# Combine some dictionary
dic1 = {"Name": "Frank"}
dic2 = {"Lastname": "Sinatra"}
dic3 = ChainMap(dic1, dic2)
print(dic3)


# dic.clear() 	                               It is used to delete all the items of the dictionary.
# dict.copy() 	                               It returns a shallow copy of the dictionary.
# dict.fromkeys(iterable, value = None, /) 	   Create a new dictionary from the iterable with the values equal to value.
# dict.get(key, default = "None") 	           It is used to get the value specified for the passed key.
# dict.has_key(key) 	                       It returns true if the dictionary contains the specified key.
# dict.items() 	                               It returns all the key-value pairs as a tuple.
# dict.keys() 	                               It returns all the keys of the dictionary.dict.setdefault(key,default= "None") 	It is used to set the key to the default value if the key is not specified in the dictionarydict.update(dict2) 	It updates the dictionary by adding the key-value pair of dict2 to this dictionary.
# dict.values() 	                           It returns all the values of the dictionary.
# len()
# popItem()
# pop()                                        It delete or remove a specified key-value from a dict.
# count()                                      Count the long of a dict.
# index()
