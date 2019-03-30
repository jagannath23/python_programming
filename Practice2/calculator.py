import re

# @todo make a class with functions
# @todo make a function to add or substract
while 1:
    # print("Ingresa una cuenta: ")
    operation = input()
    """ exp_reg: puede empezar con un numero y opcionalmente seguir con una operacion aritmetica
    """
    operation_values = re.findall(r'(?:[0-9]+)|(?:[/*+_=()-])', operation)
    print(type(operation_values))
    multiply_or_divide(operation_values)

    print(operation_values)


def multiply_or_divide(list_operation_values):
    for position, value in enumerate(list_operation_values):
        print("Value: " + value)
        print(list_operation_values)
        if value in ['*', '/']:
            value_taked = float(list_operation_values[position - 1])
            next_value = float(list_operation_values[position + 1])
            print("Value: {} Position: {} value_taked: {} next_value: {}".format(value, position, value_taked,
                                                                                 next_value))
            result = value_taked * next_value if value == '*' \
                else value_taked / next_value
            print("Resultado parcial: {}".format(result))
            list_operation_values[position - 1] = result
            print(list_operation_values)
            list_operation_values.remove(value)
            print(list_operation_values)
            list_operation_values.remove(list_operation_values[position])
            print(list_operation_values)
        elif value in ['+', '-']:
            continue
        else:
            continue

