# bank_account.py

# Take initial balance
balance = float(input("Enter initial balance: "))

# Take deposit amount
deposit = float(input("Enter deposit amount: "))
balance += deposit
print(f"Balance after deposit: {balance:.2f}")

# Take withdrawal amount
withdraw = float(input("Enter amount to withdraw: "))
if withdraw > balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print(f"Balance after withdrawal: {balance:.2f}")
