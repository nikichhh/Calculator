class InvalidExpressionError(Exception):
    def __init__(self, message="Invalid expression"):
        super().__init__(message)