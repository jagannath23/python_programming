import random

"""
Declarar dos variables numéricas con cualquier valor, e indicar cuál es
mayor. Indicar también si son iguales.
"""

a_number = random.randint(0, 10)
other_number = random.randint(0, 10)

print(a_number,
      "is equals to" if a_number == other_number else
      ("is greater than" if a_number > other_number else "is less than"),
      other_number)
