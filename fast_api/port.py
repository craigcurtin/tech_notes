

myPortfolio = Portfolio("VTI TLT IEI GLD DBC", expectedReturn = 0.05, portfolioName = "Moderate", riskBucket = 3)
myGoal = Goal(name="Vacation", targetYear=2027, targetValue=10000, priority="Dreams", portfolio=myPortfolio)
myAccount=Account(number="123456789", accountType="Taxable", accountStatus=AccountStatus("APPROVED"), cashBalance=11.0)
myAccount.goals.append(myGoal)

newOrder = Order(account=myAccount, goal=myGoal, transactionType=TransactionType("BUY"), dollarAmount=10.0)
print(newOrder.checkOrderViability())


