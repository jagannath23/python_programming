import re

HIGH_PRIORITY = 1
MEDIUM_PRIORITY = 2
LOW_PRIORITY = 3


class Calculator:
    complete_operation = []
    result = 0

    def set_operation_values(self):
        print("Enter an account: ")
        operation = input()
        # get the numerical and arithmetic values ​​of the operation
        # @todo can separation by groups be applied?
        self.complete_operation = re.findall(r'(?:[0-9]+)|(?:[/*+_=()-])', operation)

    def get_operation_values(self):
        return self.complete_operation

    def calculate(self, operation_priority):
        # save the arithmetic symbols in an array according to the priority of the operation
        symbols = ['*', '/'] if operation_priority == MEDIUM_PRIORITY else ['+', '-']

        # the values ​​of the operation are iterated
        for position, value in enumerate(self.get_operation_values()):
            # if the value is an arithmetic symbol, the operation is evaluated according to this symbol
            if value in symbols:
                arithmetic_symbol = value
                # the number before the symbol is taken
                value_taken = float(self.complete_operation[position - 1])
                # the number following the symbol is taken
                next_value = float(self.complete_operation[position + 1])

                # the operation is evaluated according to the priority
                self.result = self.evaluate_operation(value_taken, next_value, arithmetic_symbol, operation_priority)

                # the values ​​of the complete operation array are updated
                ''' the result is placed at the beginning of the complete operation array, 
                the arithmetic symbol and the next value that were already used are removed '''
                self.complete_operation[position - 1] = str(self.result)
                self.complete_operation.remove(arithmetic_symbol)
                self.complete_operation.remove(self.complete_operation[position])

    @staticmethod
    def evaluate_operation(value_taken, next_value, arithmetic_symbol, operation_priority):
        return (value_taken * next_value if arithmetic_symbol == '*' else value_taken / next_value) \
            if operation_priority == MEDIUM_PRIORITY \
            else (value_taken + next_value if arithmetic_symbol == '+' else value_taken - next_value)


calculator = Calculator()
while 1:
    med_priority_count = 0
    low_priority_count = 0

    # the user enters an operation to calculate
    calculator.set_operation_values()
    # the number of calculations for each type of operation is counted according to its priority
    for operation_value in calculator.get_operation_values():
        if operation_value in ['*', '/']:
            med_priority_count += 1
        if operation_value in ['+', '-']:
            low_priority_count += 1

    # @todo add high priority operations

    # medium priority operations are calculated
    while med_priority_count > 0:
        calculator.calculate(MEDIUM_PRIORITY)
        med_priority_count -= 1

    # low priority operations are calculated
    while low_priority_count > 0:
        calculator.calculate(LOW_PRIORITY)
        low_priority_count -= 1

    print("= {}".format(calculator.result))
