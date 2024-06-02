import random

banks = {
    1: "Chase Bank",
    2: "Capital One",
    3: "Tyme Bank",
    4: "African Bank",
    5: "Capitec",
    6: "Absa",
    7: "FNB"
}

account_types = {
    1: "Savings",
    2: "Checking",
    3: "Transaction"
}

def generate_account_number(bank, account_type):
    if bank == 1:  # Chase Bank
        account_length = 9  # Change the length for Chase Bank account numbers if necessary
    elif bank == 2:  # Capital One
        account_length = 9  # Change the length for Capital One account numbers if necessary
    elif bank == 3:  # Tyme Bank
        account_length = 9  # Change the length for Tyme Bank account numbers if necessary
    elif bank == 4:  # African Bank
        account_length = 9  # Change the length for African Bank account numbers if necessary
    elif bank == 5:  # Capitec
        account_length = 9  # Change the length for Capitec account numbers if necessary
    elif bank == 6:  # Absa
        account_length = 9  # Change the length for Absa account numbers if necessary
    elif bank == 7:  # FNB
        account_length = 9  # Change the length for FNB account numbers if necessary
    else:
        raise ValueError("Invalid bank selection.")

    # Here you can include different account types if needed

    account_number = ''.join([str(random.randint(0, 9)) for _ in range(account_length)])
    return account_number

if __name__ == "__main__":
    print("Select a bank:")
    for key, value in banks.items():
        print(key, "-", value)

    bank_choice = int(input("Enter the number corresponding to the bank you want to generate an account number for: "))

    if bank_choice not in banks:
        print("Invalid bank selection.")
    else:
        print("Select the type of account:")
        for key, value in account_types.items():
            print(key, "-", value)

        account_type_choice = int(input("Enter the number corresponding to the type of account you want to generate: "))

        if account_type_choice not in account_types:
            print("Invalid account type selection.")
        else:
            print("Generated Account Number:", generate_account_number(bank_choice, account_type_choice))