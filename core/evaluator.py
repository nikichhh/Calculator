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
                try:
                    result = self.ops[token](a, b)

                    # Handle overflow / underflow manually
                    if abs(result) > 1e308:  # overflow
                        result = float('inf')
                    elif 0 < abs(result) < 1e-308:  # underflow
                        result = 0.0

                    stack.append(result)
                except OverflowError:
                    # Directly convert to scientific notation string
                    stack.append(f"{a} {token} {b} -> Overflow")
        
        # Final result
        result = stack[0] if stack else None

        # If it's a float, format nicely in scientific notation
        if isinstance(result, float):
            return f"{result:.6g}"  # auto-switches to scientific notation if needed
        return result
