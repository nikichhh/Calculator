import math
from .functions import Function

class Pow(Function):
    name = "pow"
    arg_spec = 2
    def evaluate(self, *args):
        return math.pow(args[0], args[1])

class Sqrt(Function):
    name = "sqrt"
    arg_spec = 1
    def evaluate(self, x):
        return math.sqrt(x)
    
class Cbrt(Function):
    name = "cbrt"
    arg_spec = 1
    def evaluate(self, x):
        return math.cbrt(x)