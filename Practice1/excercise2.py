import random

"""
Declarar dos variables numéricas con cualquier valor, e indicar cuál es
mayor. Indicar también si son iguales.
"""

a_number = random.randint(0, 10)
other_number = random.randint(0, 10)

print(a_number,
      ("es mayor que" if a_number > other_number else "es menor que")
      if a_number != other_number else "es igual a",
      other_number)
