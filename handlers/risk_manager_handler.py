from handlers.handler import AbstractHandler
from trade_signal.trade_signal import TradeSignal


class RiskManagerHandler(AbstractHandler):

    def __init__(self):
        self.account_balance = 5
        self.short_trading_flag = False

    def evaluate_risk(self, trade_signal: TradeSignal):
        if trade_signal.signal is "BUY":
            cost_of_operation = trade_signal.quantity * trade_signal.ask_price
            if cost_of_operation > self.account_balance:
                print(f"Insufficient balance to purchase {trade_signal.ticker} \n Operation needs ${cost_of_operation} but "
                      f"current balance is ${self.account_balance}")
                trade_signal.signal = None
        elif trade_signal.signal is "SELL" and self.short_trading_flag is False:
            print(f"Aborting sale of {trade_signal.ticker} - Short Selling is disabled ")
            trade_signal.signal = None

    def handle(self, trade_signal: TradeSignal) -> None:
        self.evaluate_risk(trade_signal)
        super().handle(trade_signal)
