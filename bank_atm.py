def printmenu():
    print("======================")
    print("Welcome to Dons Bank")
    print("What can I do for you?")
    print("1 - Withdraw Funds")
    print("2 - Deposit Funds")
    print("3 - Show Balance")
    print("4 - Quit")


def main():
    myBalance = 1000
    userChoice = 0
    while userChoice != 4:
        printmenu()
        try:
            userChoice = int(input("Please choose one of the above options: "))
        except ValueError:
            print("That option is not valid. Please enter a valid option!")
        if userChoice == 1:
            invalid = True
            while invalid:
                try:
                    amount = int(input("Amount to withdraw:"))
                    while amount < 0:
                        print("Please enter a positive number!")
                        amount = int(input("Amount to withdraw: "))
                    while myBalance - amount < 0:
                        print("Sorry: you don't have that much money in your account.")
                        amount = int(input("Amount to withdraw: "))
                    myBalance = myBalance - amount
                    print("New balance: ", myBalance)
                    invalid = False
                except ValueError:
                    print("That option is not valid. Please enter a valid option!")
        elif userChoice == 2:
            invalid = True
            while invalid:
                try:
                    amount = int(input("Amount to deposit: "))
                    while amount < 0:
                        print("Please enter a positive number!")
                        amount = int(input("Amount to deposit: "))
                    myBalance = myBalance + amount
                    print("New balance: ", myBalance)
                    invalid = False
                except ValueError:
                    print("That option is not valid. Please enter a valid option!")
        elif userChoice == 3:
            print("Balance: ", myBalance)
        elif userChoice == 4:
            continue
        else:
            print("Invalid option.  Please choose an option by entering 1, 2, 3, or 4.")
        print("Thank you. Goodbye!")


main()


