from sympy import Eq, solve, sympify

from .tokenizer import Tokenizer
from .parser import Parser
from .evaluator import Evaluator

class Calculator:
    def __init__(self):
        pass

    def calculate(self, expression: str):
        if any(ch.isalpha() for ch in expression) or '=' in expression:
            return self._handle_symbolic(expression)
        return self._handle_numeric(expression)
    
    def _handle_numeric(self, expression: str):
        """Use Shunting Yard Algorithm for plain numeric math."""
        """The time complexity is O(n)"""
        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()

        parser = Parser(tokens)
        postfix = parser.to_postfix()

        evaluator = Evaluator(postfix)
        return evaluator.evaluate()
    
    def _handle_symbolic(sel, expression: str):
        """Use SymPy for math problems with variables or equations"""
        if '=' in expression:
            left, right = expression.split('=')
            left_expr = sympify(left)
            right_expr = sympify(right)

            vars_in_expr = list(left_expr.free_symbols.union(right_expr.free_symbols))
            equation = Eq(left_expr, right_expr)
            solution = solve(equation, vars_in_expr)
            return solution
        
        return sympify(expression)
