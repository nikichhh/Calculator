class NumberTooLargeError(Exception):
    def __init__(self, message="Number too large"):
        super().__init__(message)