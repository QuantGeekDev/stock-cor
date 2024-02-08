from handlers.handler import AbstractHandler
from trade_signal.trade_signal import TradeSignal


class OrderExecutionHandler(AbstractHandler):
    def handle(self, trade_signal: TradeSignal):
        if trade_signal.signal:
            print(f"Order Executed: {trade_signal.signal} {trade_signal.ticker}. {trade_signal.quantity} share at ${trade_signal.ask_price} ")
            super().handle(trade_signal)