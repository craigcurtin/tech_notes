class Goal(object):
    def __init__(self, name, targetYear, targetValue, initialContribution=0, monthlyContribution=0, priority=""):
        self.name = name
        self.targetYear = targetYear
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution
        if not (priority == "") and not (priority in ["Dreams", "Wishes", "Wants", "Needs"]):
            raise ValueError('Wrong value set for Priority.')
        self.priority = priority

    def getGoalProbabilities(self):
        if (self.priority == ""):
            raise ValueError('No value set for Priority.')
        import pandas as pd
        lookupTable = pd.read_csv('./Data/Goal Probability Table.csv')
        match = (lookupTable['Realize'] == self.priority)
        minProb = lookupTable['MinP'][(match)]
        maxProb = lookupTable['MaxP'][(match)]
        return minProb.values[0], maxProb.values[0]
