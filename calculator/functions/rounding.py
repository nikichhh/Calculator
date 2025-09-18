import math
from .functions import Function

class Floor(Function):
    name = "floor"
    arg_spec = 1
    def evaluate(self, x):
        return math.floor(x)
    
class Ceil(Function):
    name = "ceil"
    arg_spec = 1
    def evaluate(self, x):
        return math.ceil(x)
    
class Round(Function):
    name = "round"
    arg_spec = 1
    def evaluate(self, x):
        return round(x)
    