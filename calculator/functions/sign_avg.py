from .functions import Function

class Sign(Function):
    name = "sign"
    arg_spec = 1
    def evaluate(self, x):
        return (x > 0) - (x < 0)
    
class Avg(Function):
    name = "avg"
    arg_spec = -1
    def evaluate(self, *args):
        return sum(args) / len(args)
    
