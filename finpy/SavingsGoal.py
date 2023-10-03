
class SavingsGoal:
  def __init__(self, name, targetDate, targetValue, initialContribution, monthlyContribution):
    from dateutil import parser
    targetDateTime = parser.parse(targetDate)
    from dateutil.relativedelta import relativedelta
    delta = relativedelta(targetDateTime, date.today())
    difference_in_months = delta.months + delta.years * 12
    value = initialContribution + (monthlyContribution * difference_in_months)
    print(value)
    if not (value >= targetValue):
            raise ValueError('Target value too high to be achieved.')
    self.name = name
    self.targetDate = targetDateTime
    self.targetValue = targetValue
    self.initialContribution = initialContribution
    self.monthlyContribution = monthlyContribution
