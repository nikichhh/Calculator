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
    
class ASin(Function):
    name = "asin"
    arg_spec = 1
    def evaluate(self, x): 
        return math.asin(x)

class ACos(Function):
    name = "acos"
    arg_spec = 1
    def evaluate(self, x): 
        return math.acos(x)

class ATan(Function):
    name = "atan"
    arg_spec = 1
    def evaluate(self, x): 
        return math.atan(x)
    
class Sinh(Function):
    name = "sinh"
    arg_spec = 1
    def evaluate(self, x):
        return math.sinh(x)

class Cosh(Function):
    name = "cosh"
    arg_spec = 1
    def evaluate(self, x):
        return math.cosh(x)
    
class Tanh(Function):
    name = "tanh"
    arg_spec = 1
    def evaluate(self, x): 
        return math.tanh(x)