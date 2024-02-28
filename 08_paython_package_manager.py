### gestion de paquetes/modulos

# pip   https://pypi.org

import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

import pandas # pip install pandas
import requests
"""
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())
"""
# Arithmetics package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))
























































