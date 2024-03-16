class ExpenseSharingApp:
    def __init__(self):
        self.roommates = []

    def get_roommates(self):
        num = int(input("Enter number of roommates: "))
        for i in range(num):
            name = input(f"Enter roommate {i+1} name: ").capitalize()
            self.roommates.append(name)

    def split_bills(self, total_amount):
        if total_amount <= 0:
            print("Error: Total amount must be positive.")
            return

        amount_per_person = total_amount / len(self.roommates)
        amount_per_person = round(amount_per_person, 2)

        print("\nExpense sharing:")
        for roommate in self.roommates:
            print(f"{roommate}: ₹{amount_per_person}")

    def track_payments(self):
        paid_list = set()

        print("\nEnter the names of roommates who have paid (press Enter to finish):")
        while True:
            name = input().strip().capitalize()
            if not name:
                break
            if name not in self.roommates:
                print(f"Error: {name} is not a valid roommate.")
            else:
                paid_list.add(name)

        print("\nPayment status:")
        for roommate in self.roommates:
            status = "Paid" if roommate in paid_list else "Not Paid"
            print(f"{roommate}: {status}")


if __name__ == "__main__":
    print("\nExpense Tracker App\n")
    
    app = ExpenseSharingApp()

    # Get roommates
    app.get_roommates()

    # Get total bill amount
    total_amount = float(input("\nEnter total bill amount: "))

    # Split bills
    app.split_bills(total_amount)

    # Track payments
    app.track_payments()
