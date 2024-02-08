from handlers.risk_manager_handler import RiskManagerHandler
from handlers.signal_handler import SignalHandler
from trade_signal.trade_signal import TradeSignal
from handlers.display_handler import DisplayHandler
from handlers.order_execution_handler import OrderExecutionHandler
from handlers.risk_manager_handler import RiskManagerHandler


signal_handler = SignalHandler()
display_handler = DisplayHandler()
order_execution_handler = OrderExecutionHandler()
risk_manager_handler = RiskManagerHandler()

trade_signal = TradeSignal(ticker="AAPL", quantity=1, ask_price=5, bid_price=4.5, volume_weighted_average_price=4.75)
trade_signal2 = TradeSignal(ticker="GLD", quantity=1, ask_price=3, bid_price=6, volume_weighted_average_price=6)
trade_signal3 = TradeSignal(ticker="NVDA", quantity=1, ask_price=1, bid_price=2, volume_weighted_average_price=1.5)
trade_signal4 = TradeSignal(ticker="MSFT", quantity=1, ask_price=10, bid_price=9.5, volume_weighted_average_price=9.75)
trade_signal5 = TradeSignal(ticker="TSLA", quantity=1, ask_price=15, bid_price=14, volume_weighted_average_price=14.65)
trade_signal6 = TradeSignal(ticker="AAPL", quantity=1, ask_price=5, bid_price=4.5, volume_weighted_average_price=3.75)
trade_signal7 = TradeSignal(ticker="GLD", quantity=1, ask_price=3, bid_price=6, volume_weighted_average_price=6)
trade_signal8 = TradeSignal(ticker="NVDA", quantity=1, ask_price=1, bid_price=2, volume_weighted_average_price=1.5)

signals = [trade_signal, trade_signal2, trade_signal3, trade_signal4, trade_signal5]

if __name__ == "__main__":
    signal_handler.set_next(display_handler).set_next(risk_manager_handler).set_next(order_execution_handler)

    for trade_signal in signals:
        signal_handler.handle(trade_signal)
