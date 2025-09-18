from .trig import *
from .log_exp import Log, Exp
from .pow_root import Pow, Sqrt, Cbrt
from .rounding import Floor, Ceil, Round
from .sign_avg import Sign, Avg
from .misc import Max, Min, Abs

# register all functions
all_functions = {f.name: f for f in [
    # trigonometrical
    Sin(), Cos(), Tan(),
    ASin(), ACos(), ATan(),
    Sinh(), Cosh(), Tanh(),

    # logarithmic
    Log(), Exp(),

    # Power and root
    Pow(), Sqrt(), Cbrt(),

    # rounding
    Floor(), Ceil(), Round(),

    # sign and average
    Sign(), Avg(),

    # Others
    Max(), Min(), Abs()
]}