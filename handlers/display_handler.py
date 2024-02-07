from handlers.handler import AbstractHandler
from trade_signal.trade_signal import TradeSignal


class DisplayHandler(AbstractHandler):
    def handle(self, trade_signal: TradeSignal):
        if trade_signal.signal and isinstance(trade_signal, TradeSignal):
            print(f"New Signal! {trade_signal.ticker}: {trade_signal.signal}")
        super().handle(trade_signal)
