import random

"""
Crear una variable numérica con cualquier valor, he indicar si está entre 0 y 10.
"""

number = random.randint(0, 20)

print(number, (
    "it is between 0 and 10" if 0 < number < 10
    else "it isn't between 0 and 10"
))
