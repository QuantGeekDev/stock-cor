import datetime
from dataclasses import dataclass


@dataclass
class TradeSignal:
    """ Class for holding information regarding the generated TradeSignal"""
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.timestamp = datetime.now()

