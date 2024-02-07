from handlers.handler import AbstractHandler
from trade_signal.trade_signal import TradeSignal


class SignalHandler(AbstractHandler):
    @staticmethod
    def determine_order(trade_signal: TradeSignal):
        volume_weighted_average_price = trade_signal.volume_weighted_average_price
        if volume_weighted_average_price > 6:
            trade_signal.signal = "SELL"
        elif volume_weighted_average_price > 5:
            trade_signal.signal = None
        elif volume_weighted_average_price < 5:
            trade_signal.signal = "BUY"

        return trade_signal

    def handle(self, trade_signal: TradeSignal):
        print(f"Handling TradeSignal for {trade_signal.ticker}")
        trade_signal = self.determine_order(trade_signal)
        super().handle(trade_signal)
