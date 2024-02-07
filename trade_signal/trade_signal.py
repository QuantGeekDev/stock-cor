import datetime
from dataclasses import dataclass


@dataclass
class TradeSignal:
    """ Class for holding information regarding the generated TradeSignal"""

    ticker: str
    quantity: float
    ask_price: float
    bid_price: float
    volume_weighted_average_price: float
    signal: str
    timestamp: datetime

    def __init__(self, ticker, quantity, ask_price, bid_price, volume_weighted_average_price):
        self.ticker = ticker
        self.quantity = quantity
        self.volume_weighted_average_price = volume_weighted_average_price
        self.ask_price = ask_price
        self.bid_price = bid_price
        self.timestamp = datetime.datetime.now()


