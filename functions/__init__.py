from .trig import Sin, Cos, Tan
from .log_exp import Log, Exp
from .misc import Max, Min, Abs

# register all functions
all_functions = {f.name: f for f in [
    Sin(), Cos(), Tan(),
    Log(), Exp(),
    Max(), Min(), Abs()
]}