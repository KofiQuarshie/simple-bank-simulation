"""
Module: acct_management.py
Purpose: this file contains the code to enable the user to perform actions on the account. 
Actions include depositing, withdrawals of money, viewong account balance and account security by the use of password pins. All accounts
are stored in a text file.
         
Author: Kofi Quarshie
Date: January 6th, 2025

Dependencies:
    - Python Standard Library (random)
"""


import random

accounts = {}  # dictionary to store accounts
file_accounts = {}      #dictionary to store accounts from file


"""
function to randomly generate 7 digit integer - account numbers
"""
def random_acct_numbers():
    while True:
        #generate 7 digit account numbers if it does not already exist
        acct_number = random.randint(1000000, 9999999)
        if acct_number not in accounts:
            return acct_number
        


"""
function to enable a user to create an account which consists of a name, initial deposit, randomly generated account
number and a secure 4 digit pin and stored in the account dictionary
"""
def create_account():
    acct_name = str(input("Enter the name of the Account holder: "))
    ##error handling technique, incase user enters a string
    while True:
        try:
            acct_balance = float(input("Enter the balance you would like to start with: £"))
            break
        except ValueError:
            print("Invalid Account balance. Try again")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    while True:
        try:
            acct_pin = input("Enter a 4-digit pin: ")
            #ensures user pin has 4 digits 
            if len(acct_pin) == 4 and acct_pin.isdigit():
                print("Account pin accepted!")
                break
            else:
                print("Invalid Account pin format. Try again")
        except ValueError:
            print("Invalid Account pin format. Try again")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    acct_number = random_acct_numbers()


    # Store account as a dictionary
    account = {
        "Account Holder": acct_name,
        "Account Balance": acct_balance,
        "Account Number": acct_number,
        "Account Pin": acct_pin
    }
    #use Account number as a Key in the dictionary
    accounts[acct_number] = account

    print(f"Account created!")
    print(f"Account Holder's name: {acct_name}")
    print(f"Account Balance: £{acct_balance}")
    print(f"Account Number: {acct_number}")

    # Save account data to a file
    with open("bank_database.txt", "a") as file:
        file.write(f"\nAccount Holder: {acct_name}")
        file.write(f"\nAccount Balance: £{acct_balance}")
        file.write(f"\nAccount Number: {acct_number}")
        file.write(f"\nAccount Pin: {acct_pin}")
        file.write("\n------")

    return account  # Return the dictionary with account details


"""
Debugging function to check if created accounts are stored in the account's dictionary with their key
"""
def check_accounts():
    if not accounts:
        print("Accounts list is empty")
    else:
        for account in accounts:
            print(account)

"""
function to parse the file to load the account data and to be reused in other functions
"""
def file_parsing():
    with open("bank_database.txt", "r") as file:
        for line in file:
            if line.startswith("Account Holder"):
                #to display the value of the account holder
                file_account_name = line.split(":")[1].strip()
            elif line.startswith("Account Balance"):
                file_account_balance = line.split(":")[1].strip()
                #to display the value after the account balance
                file_account_balance = float(line.split("£")[1].strip())
            elif line.startswith("Account Number:"):
                file_account_number = int(line.split(":")[1].strip())
            elif line.startswith("Account Pin:"):
                file_account_pin = int(line.split(":")[1].strip())
                #to establish the end of a specific account's data
            elif line.strip() == "------":
                #stored as a dictionary with account number as a key
                file_account = {
                    "Account Holder": file_account_name,
                    "Account Number": file_account_number,
                    "Account Balance": file_account_balance,
                    "Account Pin": file_account_pin
                }
                file_accounts[file_account_number] = file_account

"""
function to enable the user to deposit money into the account and update the file simultenously
"""
def deposit_money():

    #reuse file parsing function
    file_parsing()

    while True:
            #error handling
            while True:
                try:
                    deposit_account = int(input("Enter the account number to deposit money into: "))
                    break
                except ValueError:
                    print("Invalid Account Number format")
                except Exception as e:
                    print(f"An unexpected error occured: {e}")

            deposit_pin = int(input("Enter the pin: "))

            if deposit_account in file_accounts and deposit_pin == file_accounts[deposit_account]["Account Pin"]:
                file_account = file_accounts[deposit_account]
                print(f"Your balance is: £",file_account["Account Balance"])

                while True:
                    try:
                        deposit = float(input("Enter the amount to deposit into your account: £"))
                        if deposit <= 0:
                            print("Deposit must be greater than 0, try again")
                        else:
                            break
                    except ValueError:
                        print("Invalid deposit amount. Try again")
                    except Exception as e:
                        print(f"An unexpected error occured: {e}")
                                
                file_account["Account Balance"] += deposit
                print(f"Deposit successful! Account {file_account['Account Number']} has a new balance of: £{file_account['Account Balance']}")

                with open("bank_database.txt", "r") as file:
                    lines = file.readlines()

                #writing and updating any deposit made into accounts in the text file
                with open("bank_database.txt", "w") as file:
                    file_account_updated = False
                    for line in lines:
                        if line.startswith(f"Account Number: {deposit_account}"):
                            file_account_updated = True
                            file.write("\nAccount Holder: " + file_account["Account Holder"])
                            file.write("\nAccount Balance: £"+str(file_account["Account Balance"]))
                            file.write("\nAccount Number: " + str(file_account["Account Number"]))
                            file.write("\nAccount Pin: " + str(file_account["Account Pin"]))
                            file.write(f"\n------")
                        else:
                            file.write(line)
                break
            else:
                print(f"Account number {deposit_account} not found. Please try again.")

"""
function to enable the user to withdraw money into the account and update the file simultenously
"""
def withdraw_money():
    
    file_parsing()

    while True:
        while True:
            try:
                withdraw_account = int(input("Enter the account to withdraw money from: "))
                break
            except ValueError:
                print("Invalid Account Number format")
            except Exception as e:
                print(f"An unexpected error occured: {e}")

        withdraw_pin = int(input("Enter your pin: "))

        if withdraw_account in file_accounts and file_accounts[withdraw_account]["Account Pin"] == withdraw_pin:
            file_account = file_accounts[withdraw_account]
            print("Your account balance is: £",file_account["Account Balance"])
            while True:
                try:
                    withdraw = float(input("Enter the amount to withdraw from your account: £"))
                    break
                except ValueError:
                    print("Invalid withdrawal amount. Try again")
                except Exception as e:
                    print(f"An unexpected error occured: {e}")

            if withdraw <= file_account["Account Balance"]:
                print("Withdrawal successful!")
                file_account["Account Balance"] -= withdraw
                print(f"Your new balance is: £{file_account['Account Balance']}")
            else:
                print("Insufficient funds. Try again")

                
            with open("bank_database.txt", "r") as file:
                lines = file.readlines()


            with open("bank_database.txt", "w") as file:
                file_account_updated = False
                for line in lines:
                    if line.startswith(f"Account Number: {withdraw_account}"):
                        file_account_updated = True
                        file.write("\nAccount Holder: " + file_account["Account Holder"])
                        file.write(f"\nAccount Balance: £"+str(file_account["Account Balance"]))
                        file.write("\nAccount Number: " + str(file_account["Account Number"]))
                        file.write("\nAccount Pin: " + str(file_account["Account Pin"]))
                        file.write(f"\n------")
                    else:
                        file.write(line)
            break
            
        else:
            print(f"Account number {withdraw_account} not found. Try again")


"""
function to enable the user to view money available in the account
"""
def view_balance():

    file_parsing()

    while True:
        while True:
            try:
                display_balance_account = int(input("Enter the Account Number to display the balance: "))
                break
            except ValueError:
                print("Invalid Account Number format")
            except Exception as e:
                print(f"An unexpected error occured: {e}")
        
        display_balance_pin = int(input("Enter your pin: "))

        if display_balance_account in file_accounts and file_accounts[display_balance_account]["Account Pin"] == display_balance_pin:
            file_account = file_accounts[display_balance_account]
            print("Your balance is: £",file_account["Account Balance"])
        else:
            print("Account not found")

        break