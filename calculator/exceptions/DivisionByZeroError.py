class DivisionByZeroError(Exception):
    def __init__(self, message="Can't devide by zero"):
        super().__init__(message)