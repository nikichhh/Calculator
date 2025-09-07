class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def to_postfix(self):
        """Convert infix tokens to postfix (RPN) using Shunting Yard Algorithm."""
        output = []
        stack = []

        for token in self.tokens:
            if token.isnumeric() or "." in token:  # number
                output.append(token)
            elif token in self.precedence:  # operator
                while stack and stack[-1] in self.precedence and \
                        self.precedence[stack[-1]] >= self.precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('
                if stack and stack[-1].isalpha(): # functions before '(')
                    output.append(stack.pop())
            elif token.isalpha():  # function name(sin, cos, log, ...)
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output
