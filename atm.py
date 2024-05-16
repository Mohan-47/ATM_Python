import time

print("Please insert your CARD")
time.sleep(1.5)

user_id = input("Enter your User ID: ")
password = 1234
pin = int(input("Enter your PIN: "))

balance = 5000

trxn_history = []
if user_id == "21450" and pin == password:
    # ATM MENU

    while True:
        print(
            """ 
    1 == Balance
    2 == Withdraw
    3 == Deposit
    4 == Transfer
    5 == Transaction History
    6 == Quit 
    """
        )

        try:
            option = int(input("Please enter your choice:"))
        except:
            print("Invalid option")
            time.sleep(1)

        if option == 1:
            print("Your balance is: ", balance)
            print("===========================================================")
            time.sleep(1)

        if option == 2:
            while True:
                try:
                    withdraw_amt = int(
                        input("Please enter the amount to be withdrawn:")
                    )
                except:
                    print("Invalid amount")
                    time.sleep(1)
                    print("===========================================================")
                    continue

                if withdraw_amt > balance:
                    print("Insufficient balance")

                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                else:
                    balance = balance - withdraw_amt
                    print(f"{withdraw_amt} is debited from your account.")

                    trxn_history.append(f"Withdraw: {withdraw_amt}")
                    print("Please collect your cash")

                    time.sleep(1)
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                    break

        if option == 3:
            while True:
                try:
                    deposit_amt = int(input("Please enter the amount to be deposited:"))
                except:
                    print("Invalid amount")
                    time.sleep(1)
                    print("===========================================================")
                    continue

                if deposit_amt < 0:
                    print("Invalid amount")
                    print("===========================================================")
                    time.sleep(1)
                else:
                    balance = balance + deposit_amt
                    trxn_history.append(f"Deposit: {deposit_amt}")
                    print(f"{deposit_amt} is credited to your account.")
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                    break

        if option == 4:
            while True:
                try:
                    recipient_id = int(input("Enter the recipient's User ID: "))
                except:
                    print("Invalid User ID")
                    time.sleep(1)
                    print("===========================================================")
                    continue

                if recipient_id == user_id:
                    print("You cannot transfer money to yourself")
                    time.sleep(1)
                    print("===========================================================")
                else:
                    while True:
                        try:
                            amount = int(input("How much would you like to transfer? "))
                        except:
                            print("Invalid amount")
                            time.sleep(1)
                            continue
                        if amount > balance:
                            print("Insufficient balance")
                            time.sleep(1)
                        else:
                            balance -= amount
                            trxn_history.append(f"Transfer: {amount} to {recipient_id}")

                            print(f"You have transferred Rs.{amount} to {recipient_id}")

                            print("Your current balance is: ", balance)
                            time.sleep(1)
                            print(
                                "==========================================================="
                            )
                            break
                    break
        if option == 5:
            print("Transaction History:")
            i = 1
            for trxn in trxn_history:
                print(f"{i}.{trxn}")
                i += 1
            print("===========================================================")

        if option == 6:
            print("Thanks for using the ATM")
            break

else:
    print("Invalid User ID or PIN")
