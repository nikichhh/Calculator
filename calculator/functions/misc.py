from .functions import Function

class Max(Function):
    name = "max"
    arg_spec = -1  # variable args
    def evaluate(self, *args): 
        return max(args)

class Min(Function):
    name = "min"
    arg_spec = -1
    def evaluate(self, *args): 
        return min(args)

class Abs(Function):
    name = "abs"
    arg_spec = 1
    def evaluate(self, x): 
        return abs(x)