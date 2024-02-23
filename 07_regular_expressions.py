### expresiones regulares ###

import re

# match

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I )
print(match)
start, end = match.span()
print(my_string[start:end])

match = print (re.match("Esta no es la leccion", my_other_string))
#if not(match == None):
if match != None:               #funcions de las tres formas
#if match is not None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

#print (re.match("Esta es la leccion", my_other_string))
#print (re.match("Expresiones Regulares", my_string))

# search
    
search = re.search("leccion", my_string, re.I )
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I )
print(findall)

# split

print(re.split(":", my_string))

#sub

print(re.sub("leccion", "Leccion", my_string))
print(re.sub("Expresiones Regulares", "Regex", my_string))

# patterns

pattern = r'[l|L]eccion'
print(re.findall(pattern, my_string))

pattern = r"[l|L]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))


email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.e"
print(re.findall(pattern, email))

# email validation regular expressions

