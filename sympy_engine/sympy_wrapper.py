import sympy as sp

class SympyWrapper:
    def __init__(self):
        self.variables = {}

    def evaluate(self, expression: str):
        try:
            # Extract symbols automatically
            symbols = {str(s): sp.Symbol(str(s)) for s in sp.symbols("x y z")}
            self.variables.update(symbols)

            expr = sp.sympify(expression, locals=self.variables)
            return expr.simplify()
        except Exception as e:
            return f"SymPy Error: {e}"