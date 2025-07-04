balance = 0
transaction = []
def show_menu():
    print("\n=== Budget Tracker ===")
    print("1.add Income")
    print("2.show balance")
    print("3.add expense")
    print("4. Show Transaction history")
    print("5.exit")

while True:
    show_menu()
    choice = input("choose an option (1-5):")
    if choice == '1':
        amount = float(input("Enter your Income :"))
        balance += amount 
        transaction.append(f"Income : Rs. {amount}")
        print("Income added successfully !")
    elif choice == '2':
        print(balance)
    elif choice == '3':
        amount = float(input("Enter the expense amount :"))
        if amount <= balance:
         balance -= amount
         transaction.append(f"Expense : Rs. {amount}")
         print("Expense entry done successfully .")
        else:
            print("insufficent balance !")
    elif choice == '4':
        print(transaction)
    elif choice == '5':
        break
