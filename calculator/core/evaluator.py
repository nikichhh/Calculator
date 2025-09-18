import operator
from calculator.exceptions.DivisionByZeroError import DivisionByZeroError
from functions import all_functions
from decimal import Decimal, getcontext, Overflow, InvalidOperation, DivisionByZero

class Evaluator:
    def __init__(self):
        self.functions = all_functions
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow,
        }
        getcontext().prec = 1000

    def evaluate(self, postfix):
        stack = []

        for token in postfix:
            if isinstance(token, Decimal):  # number
                stack.append(token)

            elif token in self.ops:  # operator
                b = stack.pop()
                a = stack.pop()
                try:
                    result = self.ops[token](a, b)
                    stack.append(result)
                except DivisionByZero:
                    raise DivisionByZeroError()
                except (Overflow, InvalidOperation):
                    stack.append(float('inf'))

            elif token == 'NEG':
                a = stack.pop()
                stack.append(-a)

            elif isinstance(token, tuple):  # (func_name, args)
                func_name, argc = token
                func = self.functions[func_name]
                args = [stack.pop() for _ in range(argc)][::-1]

                try:
                    result = func.evaluate(*args)
                    stack.append(result)
                except (Overflow, InvalidOperation):
                    stack.append(float('inf'))

        return stack[0] if stack else None
