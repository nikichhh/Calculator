import operator
import math

class Evaluator:
    def __init__(self, postfix_tokens):
        self.postfix_tokens = postfix_tokens
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow,
        }

        # All trig functions expect degrees
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'log': math.log,    # natural log
            'sqrt': math.sqrt,
        }

    def evaluate(self):
        stack = []

        for token in self.postfix_tokens:
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))
            elif token in self.ops:
                b = stack.pop()
                a = stack.pop()
                try:
                    result = self.ops[token](a, b)
                    result = self._handle_overflow(result)
                    stack.append(result)
                except OverflowError:
                    stack.append(float('inf'))
            elif token in self.functions:
                a = stack.pop()
                try:
                    result = self.functions[token](a)
                    result = self._handle_overflow(result)
                    stack.append(result)
                except OverflowError:
                    stack.append(float('inf'))
            else:  # variable support later
                stack.append(token)

        result = stack[0] if stack else None
        if isinstance(result, float):
            return f"{result:.6g}"  # auto scientific notation if large/small
        return result

    def _handle_overflow(self, num):
        if abs(num) > 1e308:
            return float('inf')
        elif 0 < abs(num) < 1e-308:
            return 0.0
        return num

