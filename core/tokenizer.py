import re

class Tokenizer:
    def __init__(self):
        # Regex for numbers, identifiers (functions/variables), and operators
        self.token_pattern = r"\d+\.\d+|\d+|[a-zA-Z_]\w*|[+\-*/^(),]"

    def tokenize(self, expression: str):
        return re.findall(self.token_pattern, expression)