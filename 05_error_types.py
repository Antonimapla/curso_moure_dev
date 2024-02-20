## error types ###

# SyntaxError 

#print"Hola comunidad!"  #error
print("Hola comunidad!")

# NameError
language = "spanish"   #comentar para error
print(language)

#  IndexError
my_list = ["paython", "swift", "kotlin", "dart", "javascript"]
print(my_list[0])
print(my_list[-1])
print(my_list[4])
#print(my_list[5])# error

# ModuleNotFoundError
#import maths #error
import math

# AttributeError
#print(math.PI)     #error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"])   #error
print(my_dict["Apellido"])

# typeError
#print(my_list["0"])   error
print(my_list[0])

# ImportError
#from math import PI
from math import pi
print(pi)

# ValueError
#my_int = int("10 años")     # error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
print(4/2)
#print(4/0)  # error

