from handlers.handler import AbstractHandler


class SignalHandler(AbstractHandler):
    def __init__(self):
        self.signal = None

    def generate_signal(self):
        self.signal = "BUY"

    def handle(self, request):
        print(f"Signal: {self.signal}")
        request.append()
        super().handle(request)
