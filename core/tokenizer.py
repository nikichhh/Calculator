import re

class Tokenizer:
    def __init__(self, expression: str):
        self.expression = expression

    def tokenize(self):
        """
        Split input string into tokens:
        - numbers (3.14, 42)
        - variables (x, y, z)
        - functions (sin, cos, log, sqrt)
        - operators (+, -, *, /, ^)
        - parentheses
        """
        token_pattern = r"\d+\.?\d*|[a-zA-Z_]+|[()+\-*/^=,]"
        tokens = re.findall(token_pattern, self.expression.replace(" ", ""))
        return tokens