class Goal(object):
    def __init__(self, name: str, targetYear: int, targetValue: float, portfolio: Portfolio = None,
                 initialContribution: float = 0, monthlyContribution: float = 0, priority: str = ""):
        self.name = name
        self.targetYear = targetYear
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution
        if not (priority == "") and not (priority in ["Dreams", "Wishes", "Wants", "Needs"]):
            raise ValueError("Wrong value set for Priority.")
        self.priority = priority
        self.portfolio = portfolio

    def getGoalProbabilities(self):
        if (self.priority == ""):
            raise ValueError("No value set for Priority.")
        lookupTable = pd.read_csv("./Data/Goal Probability Table.csv")
        match = (lookupTable["Realize"] == self.priority)
        minProb = lookupTable["MinP"][(match)]
        maxProb = lookupTable["MaxP"][(match)]
        return minProb.values[0], maxProb.values[0]

