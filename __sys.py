import sys

#The sys module in Python provides various functions 
# and variables that are used to manipulate different 
# parts of the Python runtime environment. It allows 
# operating on the interpreter as it provides access 
# to the variables and functions that interact strongly 
# with the interpreter. Let’s consider the below example.

#Example:

print("===========sys argv===============\n")
print(f"sys version: {sys.version}")

for a in sys.argv:
    if sys.argv.index(a) == 0:
        print(f"The file name is: {sys.argv[sys.argv.index(a)]}")
    else:
        print(f"The {sys.argv.index(a)} argumen is: {sys.argv[sys.argv.index(a)]}")
print("===============================\n")


print("=============File input===============\n")
# stdin: It can be used to get input from the command 
# line directly. It used is for standard input. 
# It internally calls the input() method. 
# It, also, automatically adds ‘\n’ after each sentence.

for line in sys.stdin:
    if "e" == line.rstrip():
        break
    print(f"Input: {line}")

print("Exit")
print("===============================\n")


print("===========File output==========\n")
#  stdout: A built-in file object that is analogous to 
#  the interpreter’s standard output stream in Python. 
#  stdout is used to display output directly to the 
#  screen console. Output can be of any form, it 
#  can be output from a print statement, 
#  an expression statement, and even a prompt 
#  direct for input. By default, streams are 
#  in text mode. In fact, wherever a print 
#  function is called within the code, it is 
#  first written to sys.stdout and then finally 
#  on to the screen.
 
sys.stdout.write('Geeks \n')
print("===============================\n")


print("==========File error============\n")
# stderr: Whenever an exception occurs in 
# Python it is written to sys.stderr. 

def print_to_stderr(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file = sys.stderr)
 
print_to_stderr("Error\n")
print("===============================\n")


print("==========File name============\n")
#sys.argv. It’s main purpose are:

#It is a list of command-line arguments.
#len(sys.argv) provides the number of command-line arguments.
#sys.argv[0] is the name of the current Python script.
print(f"Script Executed: {sys.argv[0]}")
print("===============================\n")


print("========Modules directories===========\n")
#sys.path is a built-in variable within the sys module that 
# returns the list of directories that the interpreter will 
# search for the required module. 

#When a module is imported within a Python file, the 
# interpreter first searches for the specified module 
# among its built-in modules. If not found it looks 
# through the list of directories defined by sys.path.

#Note: sys.path is an ordinary list and can be manipulated.

print(sys.path)

# Removing the values
sys.path = []
 
# importing pandas after removing
# values
#import pandas

print(f"list modules: {sys.path}")
print("===============================\n")


print("===========List modules========\n")
#sys.modules return the name of the Python modules 
# that the current shell has imported.

print(sys.modules)

print("===============================\n")


print("==========Ref count==============\n")
#sys.getrefcount() method is used to get the 
# reference count for any given object. This 
# value is used by Python as when this value 
# becomes 0, the memory for that particular 
# value is deleted.
a = "JuanderContreras"
print(sys.getrefcount(a))

print("===============================\n")


print("===========Exit File===========\n")
# sys.exit([arg]) can be used to exit the program. The optional 
# argument arg can be an integer giving the exit or another 
# type of object. If it is an integer, zero is considered 
# “successful termination”.

if sys.stdin == 0:
    sys.exit("Bye...")
print("===============================\n")


