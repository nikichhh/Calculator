import re
from calculator.exceptions.InvalidExpressionError import InvalidExpressionError

class Tokenizer:
    def __init__(self):
        # Regex for numbers, identifiers (functions/variables), and operators
        self.token_pattern = r"\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[a-zA-Z_]\w*|[+\-*/^(),]"

    def tokenize(self, expression: str):
        tokens = re.findall(self.token_pattern, expression)
        # Flatten tuples from regex groups
        tokens = [''.join(token) if isinstance(token, tuple) else token for token in tokens]
        if "".join(tokens) != expression.replace(" ", ""):
            raise InvalidExpressionError(f"Invalid token in expression {expression}")

        return tokens