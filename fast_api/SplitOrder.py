

class SplitOrder:
  def __init__(self, originalOrder: Order, ticker: str, dollarAmount: float):

    self.originalOrder = originalOrder
    self.ticker = ticker
    self.dollarAmount = dollarAmount
    self.units = 0


