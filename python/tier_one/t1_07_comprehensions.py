transactions = [100, -50, 20, -10, 500, -5]

withdrawals = [n for n in transactions if n < 0]

transaction_types = { n : ( "Deposit" if n > 0 else "Withdrawal") for n in transactions }

large_deposits = (n for n in transactions if n > 50)

print(withdrawals)
print(transaction_types)
print(list(large_deposits))