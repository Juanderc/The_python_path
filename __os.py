import os
import pprint

print("====os.name====")
print(os.name)
print("===============\n")

print("====os.getcwd====")
print(os.getcwd())
print("===============\n")

print("====os.chdir====")
# os.chdir()
print("===============\n")

print("====os.listdir====")
print(os.listdir("/home/jaja"))
print("===============\n")

print("====os.mkdir====")
path = os.getcwd()
direc = os.path.join(path, "/data")
# make directory
os.umask(0)
# os.mkdir(direc,mode=0o777)
# print(os.listdir())

print("=====os.rmdir()====\n")
# delete directory
# os.rmdir(f'{direc}/home.txt')
print("===============\n")

print("=====os.rename()====\n")
# f = "home.txt"
# os.rename(f,"New.txt") //rename a file
print("===============\n")

print("===os.urandom====\n")
# Declaring size
size = 5
  
# Using os.urandom() method
result = os.urandom(size) 
      
# Print the random bytes string
# Output will be different everytime
print(result) 
print("===============\n")

print("=====os.system=======\n")
#excute a command in the subshell terminal.
# os.system("date") #it excute the date on console.
print("===============\n")

print("===============\n")
#os.environ in Python is a mapping object that 
# represents the user’s environmental variables. 
# It returns a dictionary having user’s 
# environmental variable as key and their 
# values as value.

pp = pprint.PrettyPrinter(width=1,compact=True)
pp.pprint(dict(os.environ))
print("===============\n")

print("======Adding an enviroment=======\n")
# # Add a new environment variable 
# os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'
  
# # Get the value of
# # Added environment variable 
# print("GeeksForGeeks:", os.environ['GeeksForGeeks'])
print("===============\n")