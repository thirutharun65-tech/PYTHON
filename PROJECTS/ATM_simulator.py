balance = int(input("Enter a balance:"))
pin = int(input())
print("Welcome to ATM Simulator")
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your balance is:", balance)
        elif choice == "2":
            deposit = int(input("Enter amount to deposit: "))
            if deposit > 0:
                balance += deposit
                print("Deposited successfully. New balance:", balance)
            else:
                print("Invalid deposit amount.")
        elif choice == "3":
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw > 0 and withdraw <= balance:
                balance -= withdraw
                print("Withdrawal successful. New balance:", balance)
            else:
                print("Invalid withdrawal amount or insufficient balance.")
        elif choice == "4":
            print("Thank you for using ATM Simulator!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")
