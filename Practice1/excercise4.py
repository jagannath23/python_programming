import random

"""
Crear una variable numérica con cualquier valor, he indicar si está entre 0 y 10.
"""

number = random.randint(0, 20)

print(number,
      ("está entre 0 y 10" if 0 < number < 10
       else "no está entre 0 y 10"))
