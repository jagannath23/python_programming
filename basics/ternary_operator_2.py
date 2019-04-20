import random

"""
A Excercise4 añadirle si la variable está entre 11 y 20, o entre 21 y 30.
"""

number = random.randint(0, 40)

print(number,
      ("it is between 0 y 10" if 0 < number < 10 else
       ("it is between 10 y 20" if 10 < number < 20 else
        ("it is between 20 y 30" if 20 < number < 30 else
         "it isn't between 0 y 30"))))
