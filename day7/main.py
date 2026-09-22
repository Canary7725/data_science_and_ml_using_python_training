# ATM Simulation Program
# Users to choose from Check balance/ Withdraw / Exit


def checkBalance(balance):
    print(f"Your current balance is {balance}")


def withdrawAmount(balance, withdraw_amount=0):
    return balance-withdraw_amount


options = """
    ------ATM Machine-----
    ----------------------
    1. Check Balance
    2. Withdraw Amount
    ----------------------
    3. Exit
"""

balance = 5000

choice = 0

while (choice != 3):
    print(options)
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        checkBalance(balance)

    elif (choice == 2):
        withdraw_amount = float(input("Enter amount to be withdrawn: "))
        if (withdraw_amount > balance):
            print(
                f"Withdrawl Amount cannot be greater than current balance. Current balance is :{balance}")
            continue
        balance = withdrawAmount(balance, withdraw_amount)

print("Thank you !")
