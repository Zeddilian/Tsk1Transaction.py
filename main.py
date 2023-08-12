import Finances as fncs

transactions = [
fncs.Transaction(543, "12.04.2012", "Debt payment"),
fncs.Transaction(34543, "30.05.2016", "Education payment"),
fncs.Transaction(76, "05.11.2007", "Store payment")]

for trnsctns in transactions:
    trnsctns.print_info()
