### file_handling ###
import os
# .txt file
txt_file = open("C:/Users/amp/curso_moure_dev/my_file.txt", "w+")    #leer y escribir

txt_file.write("Mi nombre es Brais\nMi apellido es Moure\n35 años\nMy lenguaje preferido es Paython")

#print(txt_file.read())
#print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Kotlin")
print(txt_file.readline())

txt_file.close

#os.remove("C:/Users/amp/curso_moure_dev/my_file.txt")

# .json file

import json

json.dump

json_file = open("C:/Users/amp/curso_moure_dev/my_file.json", "w+")

json_test = {
    "name":"Brais", 
    "surname":"Moure", 
    "age":35, 
    "language": ["Python", "Swift", "Kotlin"],
    "website":"https://mour.dev"}

json.dump(json_test, json_file, indent = 2 )
json_file.close()

with open("C:/Users/amp/curso_moure_dev/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("C:/Users/amp/curso_moure_dev/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
import csv

csv_file = open("C:/Users/amp/curso_moure_dev/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surneme", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "Cobol", ""])

csv_file.close()

with open("C:/Users/amp/curso_moure_dev/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
#import xlrd     # debe instalarse el modulo

# .xml  file
import xml