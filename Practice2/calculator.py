import re

HIGH_PRIORITY = 1
MEDIUM_PRIORITY = 2
LOW_PRIORITY = 3


class Calculator:
    operation_values = []
    result = 0

    def set_operation_values(self):
        print("Ingresa una cuenta: ")
        operation = input()
        self.operation_values = re.findall(r'(?:[0-9]+)|(?:[/*+_=()-])', operation)

    def get_operation_values(self):
        return self.operation_values

    def calculate(self, operation_priority):
        symbols = ['*', '/'] if operation_priority == MEDIUM_PRIORITY else ['+', '-']
        for position, value in enumerate(self.operation_values):
            if value in symbols:
                value_taked = float(self.operation_values[position - 1])
                next_value = float(self.operation_values[position + 1])

                self.result = self.get_result_med_priority_op(value_taked, next_value, value) \
                    if operation_priority == MEDIUM_PRIORITY \
                    else self.get_result_low_priority_op(value_taked, next_value, value)

                self.operation_values[position - 1] = str(self.result)
                self.operation_values.remove(value)
                self.operation_values.remove(self.operation_values[position])

    @staticmethod
    def get_result_med_priority_op(value_taked, next_value, value):
        return value_taked * next_value if value == '*' else value_taked / next_value

    @staticmethod
    def get_result_low_priority_op(value_taked, next_value, value):
        return value_taked + next_value if value == '+' else value_taked - next_value


calculator = Calculator()
while 1:
    first_qty = 0
    second_qty = 0
    calculator.set_operation_values()
    for op_value in calculator.get_operation_values():
        if op_value in ['*', '/']:
            first_qty += 1
        if op_value in ['+', '-']:
            second_qty += 1

    while first_qty > 0:
        calculator.calculate(MEDIUM_PRIORITY)
        first_qty -= 1

    while second_qty > 0:
        calculator.calculate(LOW_PRIORITY)
        second_qty -= 1

    print("Resultado final: {}".format(calculator.result))
