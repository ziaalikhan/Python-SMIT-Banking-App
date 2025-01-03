import json

# File Name To Store Accounts Data...
file_name = "myAccounts.json"
# All Account List
all_accounts = []

# Step 1: Read The File Name
try:
    with open(file_name, "r") as file:
        accounts = json.load(file)
        all_accounts = accounts
except Exception as error:
    # If file did'nt exist, add empty list
    accounts = []


def createAccount():
    print("Creating Account !")
    try:
        account_Holder_Name = input("Enter Your Name : ")
        account_phone = input("Enter Your Phone No : ")
        account_initial_balance = int(input("Enter Your Initial Balance : "))

        # Check If There is User Name It will be allow to create an account otherwise will be throw an Error...
        # Then Will Check If Initial Value in Negative will Thorw an Error...
        if account_Holder_Name:
            if account_initial_balance >= 0:
                new_account = {
                    "name": "",
                    "phone": "",
                    "initial_balance": 0,
                    "transactions": [],
                }
                if len(account_phone) > 0:
                    new_account["name"] = account_Holder_Name
                    new_account["phone"] = account_phone
                    new_account["initial_balance"] = account_initial_balance
                    if account_initial_balance > 0:
                        new_account["transactions"].append(
                            {
                                "transaction_type": "Deposit",
                                "amount": account_initial_balance,
                            }
                        )

                    accounts.append(new_account)
                    # print(accounts)
                    with open(file_name, "w") as file:
                        json.dump(accounts, file, indent=4)
                        print(
                            f"""
                            Your Account is Successfully Created!
                                - Here is The Details...
                                - Name : {new_account["name"]}: 
                                - Phone No : {new_account["phone"]}: 
                                - Initial Balance {new_account["initial_balance"]}: 
                        """
                        )
                else:
                    print("Phone Number can't be Empty while Creating Bank Account")

            else:
                print("Initial Balance can't be Negative...")
        else:
            print("Account Name can't be Empty...")
    except Exception as error:
        print(error)

    bankingSystem()


def depositMoney():
    try:
        phone = input("Enter Your Phone No : ")
        deposit_amount = int(input("Enter Your Deposit Amount : "))
        account_found = False
        if deposit_amount > 0:
            for x in all_accounts:
                if phone == x["phone"]:
                    account_found = True
                    x["initial_balance"] += deposit_amount
                    x["transactions"].append(
                        {
                            "transaction_type": "Deposit",
                            "amount": deposit_amount,
                        }
                    )

            if account_found:
                with open(file_name, "w") as file:
                    json.dump(all_accounts, file, indent=4)
            else:
                print(f"Your Account Not Found With This Mobile No : {phone}")

        else:
            print("Amount Should be Greater Than zero...")
    except Exception as error:
        print(error)

    bankingSystem()


def withdrawMoney():
    try:
        phone = input("Enter Your Phone No : ")
        withdraw_amount = int(input("Enter Your Withdraw Amount : "))
        account_found = False

        if withdraw_amount > 0:
            for x in all_accounts:
                if phone == x["phone"]:
                    account_found = True
                    if withdraw_amount <= x["initial_balance"]:
                        x["initial_balance"] -= withdraw_amount
                        x["transactions"].append(
                            {
                                "transaction_type": "Withdraw",
                                "amount": withdraw_amount,
                            }
                        )
                    else:
                        print(f"Your Balance is Less Than : {withdraw_amount}")
                        #  bankingSystem()

            if account_found:
                with open(file_name, "w") as file:
                    json.dump(all_accounts, file, indent=4)
            else:
                print(f"Your Account Not Found With This Mobile No : {phone}")

        else:
            print("Amount Should be Greater Than zero...")
    except Exception as error:
        print(error)

    bankingSystem()


def accountBalance():
    phone = input("Enter Your Phone No : ")
    account_found = False
    balance = 0
    for x in all_accounts:
        if phone == x["phone"]:
            account_found = True
            balance = x["initial_balance"]

    if account_found:
        print(f"Your Account Balance is : {balance}")
    else:
        print(f"Your Account Not Found With This Mobile No : {phone}")

    bankingSystem()


def printAccountStatement():
    phone = input("Enter Your Phone No : ")
    account_found = False

    for x in all_accounts:
        if phone == x["phone"]:
            account_found = True
            print(
                """Your Account Statement is
Transaction Type | Date | Amount"""
            )
            for j in x["transactions"]:
                print(f"""{j["transaction_type"]}  | {j["amount"]}""")

    if not account_found:
        print(f"Your Account Not Found With This Mobile No : {phone}")

    bankingSystem()


def bankingSystem():
    try:
        services = int(
            input(
                """
            Welcome to Bank, How Can We Help You!
            1: Create an Account. Press 1 for it.
            2: Deposit Money. Press 2 for it.
            3: Withdraw Money. Press 3 for it.
            4: Check Account balance. Press 4 for it.
            5: Print a transaction statement showing all deposits and withdrawals. Press 5 for it.
            6: EXIT.
        """
            )
        )

        # Check if Input is not 1,2,3,4,5 then will Thorw an Error...
        if (
            services == 1
            or services == 2
            or services == 3
            or services == 4
            or services == 5
            or services == 6
        ):
            if services == 1:
                createAccount()
            elif services == 2:
                depositMoney()
            elif services == 3:
                withdrawMoney()
            elif services == 4:
                accountBalance()
            elif services == 5:
                printAccountStatement()
            elif services == 6:
                return
            else:
                print("Some Thing Went Wrong...")
        else:
            print("Invalid Request Please Try with 1,2,3,4,5...")
    except Exception as error:
        print(error)


bankingSystem()
