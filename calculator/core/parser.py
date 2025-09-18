import re
from decimal import Decimal, InvalidOperation
from exceptions.NumberTooLargeError import NumberTooLargeError

def is_number(token):
    return bool(re.match(r'^-?\d+(\.\d+)?([eE][-+]?\d+)?$', token))

class Parser:
    def __init__(self, functions, operators):
        self.functions = functions
        self.operators = operators

    def to_postfix(self, tokens):
        output = []
        stack = []
        arg_count_stack = []

        for i, token in enumerate(tokens):
            try:
                output.append(Decimal(token))
                continue
            except (InvalidOperation, ValueError):
                if is_number(token):
                    raise NumberTooLargeError(f"Number is too large {token}")

            if token in self.functions:
                stack.append(token)
                arg_count_stack.append(1)

            elif token == '-':
                # Detect unary
                if i == 0 or tokens[i - 1] in self.operators or tokens[i - 1] == '(' or tokens[i - 1] in self.functions:
                    # Unary minus -> treat as "NEG" operator
                    while (stack and stack[-1] in self.operators):
                        prec2, assoc2 = self.operators[stack[-1]]
                        prec1, assoc1 = self.operators["NEG"]
                        if (assoc1 == 'L' and prec1 <= prec2) or (assoc1 == 'R' and prec1 < prec2):
                            output.append(stack.pop())
                        else:
                            break
                    stack.append("NEG")
                else:
                    # Normal binary minus (your existing precedence code)
                    prec1, assoc1 = self.operators[token]
                    while (stack and stack[-1] in self.operators):
                        prec2, assoc2 = self.operators[stack[-1]]
                        if (assoc1 == 'L' and prec1 <= prec2) or (assoc1 == 'R' and prec1 < prec2):
                            output.append(stack.pop())
                        else:
                            break
                    stack.append(token)

            elif token == ',':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if arg_count_stack:
                    arg_count_stack[-1] += 1

            elif token in self.operators:
                while (stack and stack[-1] in self.operators and
                       self.operators[stack[-1]][0] >= self.operators[token][0]):
                    output.append(stack.pop())
                stack.append(token)

            elif token == '(':
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('

                if stack and stack[-1] in self.functions:
                    func = stack.pop()
                    argc = arg_count_stack.pop()
                    output.append((func, argc))

        while stack:
            output.append(stack.pop())

        return output
