class Transaction:
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

    def print_info(self):
        print(f"Date {self.date}, Amount {self.amount}, Description {self.description}")
