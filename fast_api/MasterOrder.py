
# Master Order class that maintains ref. to split to original.
# Some ID to track back to splitOrders?
# Update status of originalOrder(s)
class MasterOrder:
  def __init__(self, status: OrderStatus=OrderStatus("NEW")):

    self.splitOrders = []
    self.masterTable = pd.DataFrame(columns=['Account','Symbol','Type','DollarAmount'])
    self.status = status

  def addSplitOrder(self, splitOrder: SplitOrder):
    self.splitOrders.append(splitOrder)

  def aggregate(self) -> pd.DataFrame:
    for split in self.splitOrders:
      new_row = {'Account':split.originalOrder.account.number,'Symbol':split.ticker,'Type':split.originalOrder.transactionType.value,'DollarAmount':split.dollarAmount}
      self.masterTable = self.masterTable.append(new_row, ignore_index=True)

    return self.masterTable.groupby(['Symbol','Type']).sum().reset_index()


  def orderSent(self):
    newStatus = OrderStatus("PENDING")
    self.status = newStatus
    for split in self.splitOrders:
      split.originalOrder.status = newStatus

  def allocateAccounts(self, filledMasterOrderFile: pd.DataFrame) -> pd.DataFrame:
    accountTable = pd.DataFrame(columns=['Account','Symbol','Type','Units'], index=self.masterTable.index)
    for index, row in filledMasterOrderFile.iterrows():
      ordersToAllocate = self.masterTable[(self.masterTable['Symbol'] == row['Symbol']) & (self.masterTable['Type'] == row['Type'])]
      totalValue = float(ordersToAllocate.groupby(['Symbol','Type'])['DollarAmount'].sum()[0])
      for index2, row2 in ordersToAllocate.iterrows():
        unitsAllocated = (row2['DollarAmount'] / totalValue) * row['Units']
        new_row = {'Account':row2['Account'],'Symbol':row2['Symbol'],'Type':row2['Type'],'Units':unitsAllocated}
        accountTable.iloc[index2] = new_row
        self.splitOrders[index2].units = unitsAllocated
        self.splitOrders[index2].originalOrder.account.cashBalance -= unitsAllocated * row['Price']
        #print(self.splitOrders[index2].originalOrder.account.number)
    return accountTable

  def allocateGoals(self):
    for order in self.splitOrders:
      portfolioAllocations = order.originalOrder.goal.portfolio.allocations
      #print(order.originalOrder.goal.portfolio.name)
      for idx, item in enumerate(portfolioAllocations):
        if item.ticker == order.ticker and order.originalOrder.transactionType == TransactionType("BUY"):
          order.originalOrder.goal.portfolio.allocations[idx].units += order.units
          #print(item.ticker + ": " + str(order.units))
        elif item.ticker == order.ticker and order.originalOrder.transactionType == TransactionType("SELL"):
          order.originalOrder.goal.portfolio.allocations[idx].units -= order.units

  def orderFilled(self):
    newStatus = OrderStatus("FILLED")
    self.status = newStatus
    for split in self.splitOrders:
      split.originalOrder.status = newStatus


if __name__ == '__main__':
    newMasterOrder = MasterOrder()
    for split in splitOrders:
        newMasterOrder.addSplitOrder(split)

