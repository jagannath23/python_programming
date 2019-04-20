import random

"""
Declara dos variables numéricas con cualquier valor, mostrar por consola
la suma, resta, multiplicación, exponente, división y módulo (resto de la división)
"""

a_number = random.randint(1, 20)
other_number = random.randint(1, 20)

print(a_number, "+", other_number, "=", a_number + other_number)
print(a_number, "-", other_number, "=", a_number - other_number)
print(a_number, "*", other_number, "=", a_number * other_number)
print(a_number, "**", other_number, "=", a_number ** other_number)
print(a_number, "/", other_number, "=", a_number / other_number)
print(a_number, "%", other_number, "=", a_number % other_number)
