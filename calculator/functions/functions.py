from abc import ABC, abstractmethod

class Function(ABC):
    """Base interface for all functions"""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def arg_spec(self):
        """
        - int for fixed number of args
        - tuple(min, max) for range (like 1 or 2 for log)
        - -1 for variable args (like max/min)
        """
        pass

    @abstractmethod
    def evaluate(self, *args: float) -> float:
        pass