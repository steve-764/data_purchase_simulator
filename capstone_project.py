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
    for i, bundle in enumerate(bundle, start=1):
        print(f"{i}. {bundle["name"]} | Ksh {bundle["price"]} | Valid: {bundle["validity"]}")
    print("0. Back to main menu")
    print()
    choice = input("Enter choice : ")
    return choice




# main_menu()

