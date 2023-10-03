

class WeddingGoal(SavingsGoal):
  def __init__(self, name, weddingDate, budget, initialContribution, monthlyContribution):
    super().__init__(name, weddingDate, budget, initialContribution, monthlyContribution)
    self.weddingDate = weddingDate

class TravelGoal(SavingsGoal):
  def __init__(self, destination, tripDate, tripDuration, budget, initialContribution, monthlyContribution):
    super().__init__(destination, tripDate, budget, initialContribution, monthlyContribution)
    self.tripDuration = tripDuration

class SplurgeGoal(SavingsGoal):
  def __init__(self, itemName, storeName, targetPurchaseDate, budget, initialContribution, monthlyContribution):
    super().__init__(itemName + " @ " + storeName, targetPurchaseDate, budget, initialContribution, monthlyContribution)

