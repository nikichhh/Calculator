class EmptyExpression(Exception):
    def __init__(self, message="No expression"):
        super().__init__(message)