import re

class Tokenizer:
    def __init__(self, expression: str):
        self.expression = expression

    def tokenize(self):
        """Split input string into tokens (numbers, operators, parentheses)."""
        token_pattern = r"\d+\.?\d*|[a-zA-Z]+|[()+\-*/^=]"
        tokens = re.findall(token_pattern, self.expression.replace(" ", ""))
        return tokens