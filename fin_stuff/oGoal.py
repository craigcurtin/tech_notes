class Goal(object):
    def __init__(self, name, targetYear, targetValue, initialContribution=0, monthlyContribution=0):
        self.name = name
        self.targetYear = targetYear
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution


class RetirementGoal(Goal):
    def __init__(self, name, targetValue, startingAge, retirementAge):
        targetYear = date.today().year + (retirementAge - startingAge)
        super().__init__(name, targetYear, targetValue)
        self.retirementAge = retirementAge


class GrowWealthGoal(Goal):
    def __init__(self, initialContribution, monthlyContribution):
        targetYear = date.today().year + 10
        targetAmount = 1000000
        super().__init__("Grow My Wealth", targetYear, targetAmount, initialContribution, monthlyContribution)


class EducationGoal(Goal):
    def __init__(self, name, startYear, degreeLengthYears, annualTuitionFees, degreeType, schoolName):
        targetValue = degreeLengthYears * annualTuitionFees
        super().__init__(name, startYear, targetValue)
        self.degreeType = degreeType
        self.schoolName = schoolName


class RealEstateGoal(Goal):
    def __init__(self, name, targetYear, homeValue, downPayment, mortgagePayment, interestRate):
        targetValue = downPayment
        super().__init__(name, targetYear, targetValue)
        self.homeValue = homeValue
        self.downPayment = downPayment
        self.mortgagePayment = mortgagePayment
        self.interestRate = interestRate


class StartupGoal(Goal):
    def __init__(self, companyName, startYear, seedFunding):
        super().__init__(companyName, startYear, seedFunding)
