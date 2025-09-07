from .symbolic_evaluator import SymbolicEvaluator
from .tokenizer import Tokenizer
from .parser import Parser
from .evaluator import Evaluator

class Calculator:
    def __init__(self):
        self.overflow_limit = 1e308  

    def calculate(self, expression: str):
        tokenizer = Tokenizer(expression)
        tokens = tokenizer.tokenize()

        if '=' in expression:
            return self._handle_symbolic(expression)
        
        has_variables = any(token.isalpha() and token not in self._allowed_functions() for token in tokens)
        if has_variables:
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
        symbolic = SymbolicEvaluator(expression)
        return symbolic.evaluate()
    
    def _allowed_functions(self):
        return {'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'sqrt'}
