# initializing a dictionary named bankmanagesystem
bankmanagesystem = {}

# define the add_customer function
def add_customer():
    # defining the variables in the function accordingly...
    while True:
        try:
            customer_id = int(input("Enter the customer id: "))
            break
        except ValueError:
            print("Please enter a valid integer for customer id.")
    customer_name = input("Enter the name: ")
    customer_address = input("Enter the address: ")
    print("Which type of account to be opened?:\n1. Savings\n2. Current")
    while True:
        try:
            x = int(input())
            if x == 1:
                account_type = "SAVINGS"
                break
            elif x == 2:
                account_type = "CURRENT"
                break
            else:
                print("Invalid selection. Please choose 1 or 2.")
        except ValueError:
            print("Please enter a valid number (1 or 2).")
    # Minimum balance check
    while True:
        try:
            customer_balance = float(input("Minimum balance to be maintained is 500 Rupees\nEnter the balance to start the account: "))
        except ValueError:
            print("Please enter a valid number for balance.")
            continue
        if customer_balance >= 500:
            bankmanagesystem[customer_id] = {
                "name": customer_name,
                "address": customer_address,
                "accounttype": account_type,
                "balance": customer_balance
            }
            print("Customer added successfully.")
            break
        else:
            print("You have entered an amount less than 500. Please enter again.")

# define the delete function
def delete():
    try:
        customer_id = int(input("Enter the id of the customer you want to delete: "))
    except ValueError:
        print("Invalid entry. Customer id should be a number.")
        return
    if customer_id in bankmanagesystem:
        del bankmanagesystem[customer_id]
        print("Deleted Successfully.")
    else:
        print("Customer id not found in our records.")

# define the balance function
def balance():
    try:
        customer_id = int(input("Enter the customer id: "))
    except ValueError:
        print("Invalid entry. Customer id should be a number.")
        return
    if customer_id in bankmanagesystem:
        print(f"The Balance is {bankmanagesystem[customer_id]['balance']}")
    else:
        print("Customer id not found in our records.")

# define the withdraw function
def withdraw():
    try:
        customer_id = int(input("Enter the customer id: "))
    except ValueError:
        print("Invalid entry. Customer id should be a number.")
        return
    if customer_id in bankmanagesystem:
        withdrawal_limit = 10000.0
        try:
            withdrawal_amount = float(input("Enter the amount to be withdrawn: "))
        except ValueError:
            print("Please enter a valid number for amount.")
            return
        if withdrawal_amount > withdrawal_limit:
            print("More than daily withdrawal limit.")
        elif withdrawal_amount > bankmanagesystem[customer_id]['balance']:
            print("Not enough balance.")
        else:
            bankmanagesystem[customer_id]['balance'] -= withdrawal_amount
            print(f"The new balance is {bankmanagesystem[customer_id]['balance']}")
    else:
        print("Customer not found in our records.")

# define the deposit function
def deposit():
    try:
        customer_id = int(input("Enter the customer id: "))
    except ValueError:
        print("Invalid entry. Customer id should be a number.")
        return
    if customer_id in bankmanagesystem:
        try:
            deposit_amount = float(input("Enter the amount to be deposited: "))
        except ValueError:
            print("Please enter a valid number for amount.")
            return
        bankmanagesystem[customer_id]['balance'] += deposit_amount
        print(f"The new balance is {bankmanagesystem[customer_id]['balance']}")
    else:
        print("Customer not found in our records.")

# define the detail function
def details():
    try:
        customer_id = int(input("Enter the customer id: "))
    except ValueError:
        print("Invalid entry. Customer id should be a number.")
        return
    if customer_id in bankmanagesystem:
        print(f"Name: {bankmanagesystem[customer_id]['name']}")
        print(f"Address: {bankmanagesystem[customer_id]['address']}")
        print(f"Account type: {bankmanagesystem[customer_id]['accounttype']}")
        print(f"Balance: {bankmanagesystem[customer_id]['balance']}")
    else:
        print("Customer not found in our records.")

# The main menu options function
def options():
    while True:
        print("\nSelect an option:")
        print("1. ADD NEW CUSTOMER")
        print("2. DELETE")
        print("3. BALANCE")
        print("4. WITHDRAW")
        print("5. DEPOSIT")
        print("6. PRINT DETAILS")
        print("0. EXIT")
        try:
            x = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue
        if x == 1:
            add_customer()
        elif x == 2:
            delete()
        elif x == 3:
            balance()
        elif x == 4:
            withdraw()
        elif x == 5:
            deposit()
        elif x == 6:
            details()
        elif x == 0:
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid Input. Please enter a number between 0 and 6.")

# Run the program
options()
