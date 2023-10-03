class TransactionType(object):
    def __init__(self, value: str):
        if not value in ("BUY", "SELL"):
            raise ValueError("Allowed types: BUY, SELL.")
        self.value = value

    def __eq__(self, other):
        return self.value == other.value
