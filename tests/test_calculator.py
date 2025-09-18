import unittest
from calculator.functions import all_functions
from calculator.core.tokenizer import Tokenizer
from calculator.core.parser import Parser
from calculator.core.evaluator import Evaluator
from calculator.exceptions.InvalidExpressionError import InvalidExpressionError
from calculator.exceptions.DivisionByZeroError import DivisionByZeroError
from calculator.exceptions.EmptyExpression import EmptyExpression
from exceptions.NumberTooLargeError import NumberTooLargeError


class TestCalculator(unittest.TestCase):
    def setUp(self):
        operators = {
            '+': (1, 'L'),
            '-': (1, 'L'),
            '*': (2, 'L'),
            '/': (2, 'L'),
            '^': (3, 'R'),
        }
        self.tokenizer = Tokenizer()
        self.parser = Parser(all_functions, operators)
        self.evaluator = Evaluator()
    
    def test_addition(self):
        expr = "(2+2)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 4)

    def test_subtraction(self):
        expr = "(10-3)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 7)

    def test_multiplication(self):
        expr = "(5*6)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 30)

    def test_division(self):
        expr = "(8/2)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        expr = "(5/0)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        with self.assertRaises(DivisionByZeroError):
            self.evaluator.evaluate(postfix)

    def test_empty_input(self):
        expr = ""
        with self.assertRaises(EmptyExpression):
            if not expr.strip():
                raise EmptyExpression()
            tokens = self.tokenizer.tokenize(expr)
            postfix = self.parser.to_postfix(tokens)
            self.evaluator.evaluate(postfix)

    def test_invalid_token(self):
        expr = "2 + $"
        with self.assertRaises(InvalidExpressionError):
            tokens = self.tokenizer.tokenize(expr)
            postfix = self.parser.to_postfix(tokens)
            self.evaluator.evaluate(postfix)

    def test_power(self):
        expr = "(2^3)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 8)

    def test_functions(self):
        expr = "sin(0)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertAlmostEqual(result, 0, places=5)

        expr = "abs(-7)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 7)

        expr = "max(3,7)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 7)

        expr = "min(3,7)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 3)

        expr = "log(100,10)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertEqual(result, 2)

        expr = "exp(1)"
        tokens = self.tokenizer.tokenize(expr)
        postfix = self.parser.to_postfix(tokens)
        result = self.evaluator.evaluate(postfix)
        self.assertAlmostEqual(result, 2.71828, places=5)

    def test_overflow(self):
        expr = "1e4000000000000000000"
        tokens = self.tokenizer.tokenize(expr)
        with self.assertRaises(NumberTooLargeError):
            self.parser.to_postfix(tokens)


if __name__ == "__main__":
    unittest.main()
        