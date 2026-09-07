bundles = {
    "Data": [
        {"name": "50MB - Daily",   "price": 5,   "validity": "24 hours"},
        {"name": "500MB - Weekly", "price": 50,  "validity": "7 days"},
        {"name": "2GB - Monthly",  "price": 200, "validity": "30 days"},
    ],
    "SMS": [
        {"name": "20 SMS - Daily",   "price": 5,  "validity": "24 hours"},
        {"name": "200 SMS - Weekly", "price": 20, "validity": "7 days"},
    ],
    "Minutes": [
        {"name": "10 Min - Daily",    "price": 10,  "validity": "24 hours"},
        {"name": "100 Min - Monthly", "price": 100, "validity": "30 days"},
    ],
}
 
balance = 200.00   # starting airtime balance in Ksh

def main_menu():
    print("=" * 30)
    print("           *544# ")
    print("=" * 30)
    print()
    print("1. Buy Data Bundle")
    print("2. Buy SMS Bundle")
    print("3. Buy Minutes Bundles")
    print("4. Check Balance")
    print("5. Exit")
    print("=" * 30)
    choice = input(("Enter choice (1-5): "))
    return choice


def show_bundles(category, bundle):
    print(f"--- {category.upper()} BUNDLES ---")
    for num, bundle in enumerate(bundle, start=1):
        print(f"{num}. {bundle["name"]} | Ksh {bundle["price"]} | Valid: {bundle["validity"]}")
    print("0. Back to main menu")
    print()
    choice = input("Enter choice : ")
    return choice


def buy_bundle(category, bundles, balance):
    while True:
        # calling show bundles function
        choice = show_bundles(category, bundles)

        if choice == "0":
            break

        # try catch clause to catch wrong input
        try:
            # converting str choice into int
            index = int(choice)
            if index < 1 or index > len(bundles):
                raise ValueError
        except ValueError:
            print("Ivalid choice. Enter a valid option")
            continue

        # subtracting 1 since we used enumerate function satrting at 1 in show bundles function 
        bundle = bundles[index - 1]
        confirm = input(f"Proceed with purchase of {bundle["name"]} for Ksh {bundle["price"]}? (y/n) : ")

        # using lower to standerdize input
        if confirm.lower() == "y":
            # checking if current balance > price of bundle
            if balance >= bundle["price"]:
                balance -= bundle["price"]
                print(f"Purchase of {bundle["name"]} successful! ")
                print(f"Balance : Ksh {balance}")
            else:
                print("Insufficient balance. Please top up.")
        else:
            print("Purchase cancelled.")
    return balance


def check_balance(balance):
    print(f"Current balance : Ksh {balance}")


def main():
    # using balance in the main function 
    balance = 200.00

    while True:
        choice = main_menu()

        if choice == "1":
            balance = buy_bundle("Data", bundles["Data"], balance)
        elif choice == "2":
            balance = buy_bundle("SMS", bundles["SMS"], balance)
        elif choice == "3":
            balance = buy_bundle("Minutes", bundles["Minutes"], balance)
        elif choice == "4":
            check_balance(balance)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a valid option.")


main()

    



