import math
from .functions import Function

class Sin(Function):
    name = "sin"
    arg_spec = 1
    def evaluate(self, x):
        return math.sin(x)

class Cos(Function):
    name = "cos"
    arg_spec = 1
    def evaluate(self, x):
        return math.cos(x)
    
class Tan(Function):
    name = "tan"
    arg_spec = 1
    def evaluate(self, x): 
        return math.tan(x)