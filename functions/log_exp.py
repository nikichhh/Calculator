import math
from .functions import Function

class Log(Function):
    name = "log"
    arg_spec = (1, 2)  # supports 1 or 2 args
    def evaluate(self, *args):
        if len(args) == 1:
            return math.log(args[0])  # natural log
        elif len(args) == 2:
            return math.log(args[0], args[1])  # log base b
        raise ValueError("log expects 1 or 2 arguments")

class Exp(Function):
    name = "exp"
    arg_spec = 1
    def evaluate(self, x): 
        return math.exp(x)