class Parser:
    def __init__(self, functions, operators):
        self.functions = functions
        self.operators = operators

    def to_postfix(self, tokens):
        output = []
        stack = []
        arg_count_stack = []

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output.append(float(token))

            elif token in self.functions:
                stack.append(token)
                arg_count_stack.append(1)

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
