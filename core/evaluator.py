import operator

class Evaluator:
    def __init__(self, postfix_tokens):
        self.postfix_tokens = postfix_tokens
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

    def evaluate(self):
        """Evaluate a postfix expression."""
        stack = []

        for token in self.postfix_tokens:
            if token.replace('.', '', 1).isdigit():  # number
                stack.append(float(token))
            elif token in self.ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.ops[token](a, b))

        return stack[0] if stack else None
