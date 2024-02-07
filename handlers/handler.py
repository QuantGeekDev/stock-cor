from abc import ABC, abstractmethod


class Handler(ABC):
    """Handler interface for Chain of Responsibility"""

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, trade_signal):
        pass


class AbstractHandler(Handler):
    """Abstract Handler for Chain of Responsibility"""

    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, trade_signal):
        if self._next_handler:
            return self._next_handler.handle(trade_signal)

        return None
