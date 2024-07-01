class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.categories = ["Food", "Housing", "Transportation", "Entertainment", "Other"]

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def get_balance(self):
        total_expenses = sum(self.expenses.values())
        return self.income - total_expenses

    def get_summary(self):
        summary = f"Income: ${self.income:.2f}\n"
        summary += "Expenses:\n"
        for category, amount in self.expenses.items():
            summary += f"  {category}: ${amount:.2f}\n"
        summary += f"Balance: ${self.get_balance():.2f}"
        return summary

def main():
    tracker = BudgetTracker()
    
    print("Welcome to the Interactive Budget Tracker!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add income")
        print("2. Add expense")
        print("3. View summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            amount = float(input("Enter income amount: $"))
            tracker.add_income(amount)
            print(f"Income of ${amount:.2f} added.")
        
        elif choice == "2":
            print("Expense categories:")
            for i, category in enumerate(tracker.categories, 1):
                print(f"{i}. {category}")
            cat_choice = int(input("Choose a category (1-5): ")) - 1
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(tracker.categories[cat_choice], amount)
            print(f"Expense of ${amount:.2f} added to {tracker.categories[cat_choice]}.")
        
        elif choice == "3":
            print("\nBudget Summary:")
            print(tracker.get_summary())
        
        elif choice == "4":
            print("Thank you for using the Budget Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()