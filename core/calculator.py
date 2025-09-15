from exceptions.EmptyExpression import EmptyExpression
from exceptions.InvalidExpressionError import InvalidExpressionError
from exceptions.DivisionByZeroError import DivisionByZeroError
from .tokenizer import Tokenizer
from .parser import Parser
from .evaluator import Evaluator
from functions import all_functions
from sympy_engine.sympy_wrapper import SympyWrapper

class Calculator:
    def __init__(self):
        self.operators = {
            '+': (1, 'L'),
            '-': (1, 'L'),
            '*': (2, 'L'),
            '/': (2, 'L'),
            '^': (3, 'R'),
        }
        self.tokenizer = Tokenizer()
        self.parser = Parser(all_functions, self.operators)
        self.evaluator = Evaluator()
        self.sympy_engine = SympyWrapper()

    def calculate(self, expression: str):
        expression = expression.strip()
        if not expression:
            raise EmptyExpression()
        
        try:
            tokens = self.tokenizer.tokenize(expression)

            # Check for variables (symbols not in operators/functions)
            has_variable = any(
                token.isalpha() and token not in self.operators and token not in self.parser.functions
                for token in tokens
            )

            if has_variable or "=" in expression:
                return str(self.sympy_engine.evaluate(expression))

            postfix = self.parser.to_postfix(tokens)
            result = self.evaluator.evaluate(postfix)

            if isinstance(result, float):
                return f"{result:.6g}"
            return result
        
        except EmptyExpression as e:
            return str(e)
        except DivisionByZeroError as e:
            return 'inf'
        except InvalidExpressionError as e:
            return str(e)
        except Exception as e:
            return f"Error: {e}"
