"""
Module: acct_management.py
Purpose: This file contains the code to run the entire program
         
Author: Kofi Quarshie
Date: January 6th, 2025

Dependencies:
    - acct_management.py
    - Python standard libraary (random)
"""

from acct_management import create_account, check_accounts, deposit_money, withdraw_money, view_balance

def main_menu():
    while True:
        print("-------------> WELCOME TO THE BANK <--------------")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Balance")
        print("5. Show all Accounts")
        print("6. Quit")
        print("\n")
        choices = input(("Select from the options (1-6):"))

        if choices == '1':
            create_account()

        elif choices == '2':
            deposit_money()
                
        elif choices == '3':
            withdraw_money()

        elif choices == '4':
            view_balance()

        elif choices == '5':
            check_accounts()

        elif choices == '6':
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid input, Try again.")

main_menu()
