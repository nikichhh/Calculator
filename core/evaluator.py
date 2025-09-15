import operator
from exceptions.DivisionByZeroError import DivisionByZeroError
from functions import all_functions

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

    def evaluate(self, postfix):
        stack = []

        for token in postfix:
            if isinstance(token, float):  # number
                stack.append(token)

            elif token in self.ops:  # operator
                b = stack.pop()
                a = stack.pop()
                try:
                    result = self.ops[token](a, b)
                    result = self._handle_overflow(result)
                    stack.append(result)
                except ZeroDivisionError:
                    raise DivisionByZeroError()
                except OverflowError:
                    stack.append(float('inf'))

            elif isinstance(token, tuple):  # (func_name, args)
                func_name, argc = token
                func = self.functions[func_name]
                args = [stack.pop() for _ in range(argc)][::-1]

                try:
                    result = func.evaluate(*args)
                    result = self._handle_overflow(result)
                    stack.append(result)
                except OverflowError:
                    stack.append(float('inf'))

        return stack[0] if stack else None

    def _handle_overflow(self, num):
        if abs(num) > 1e308:
            return float('inf')
        elif 0 < abs(num) < 1e-308:
            return 0.0
        return num
