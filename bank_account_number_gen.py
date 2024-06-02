import random
import time

# ANSI color escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
END = "\033[0m"

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

def show_banner():
    print(RED + "=======================================")
    print("        Bank Account Number Generator   ")
    print("                 by DroidDevHub         ")
    print("=======================================" + END)
    print()

def show_loading_screen():
    print(YELLOW + "Loading..." + END)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(END)

def show_thank_you_message():
    print(GREEN + "\nThank you for using this tool!" + END)

    print(YELLOW + "For more tools and updates, visit my " + CYAN + "GitHub: https://github.com/Techbyets" + END)
    
    
    
    print(YELLOW + "You can also join my Telegram channel: " + CYAN + " https://t.me/DroidDevHub" + END)
    

if __name__ == "__main__":
    show_loading_screen()
    show_banner()

    print("Select a bank:")
    for key, value in banks.items():
        print(CYAN + str(key) + " - " + value + END)

    bank_choice = int(input("Enter the number corresponding to the bank you want to generate an account number for: "))

    if bank_choice not in banks:
        print("Invalid bank selection.")
    else:
        print("Select the type of account:")
        for key, value in account_types.items():
            print(CYAN + str(key) + " - " + value + END)

        account_type_choice = int(input("Enter the number corresponding to the type of account you want to generate: "))

        if account_type_choice not in account_types:
            print("Invalid account type selection.")
        else:
            show_loading_screen()
            print(GREEN + "Generated Account Number:", generate_account_number(bank_choice, account_type_choice) + END)
            show_thank_you_message()
