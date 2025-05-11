import pandas as pd


class Expense:
    def __init__(self, category , amount, date, ):
        self.category= category
        self.amount= amount
        self.date=date 


class ExpenseManager:
    def __init__(self):
        self.collection = []

    def add_expense(self,expense):
        self.collection.append(expense)

    def view_expenses(self):
         if not self.collection:
            print("No expenses recorded.")
            return
       
         print("\nAll Expenses:")
         for idx, expense in enumerate(self.collection, start=1):
           print(f"{idx}. {expense.category} | {expense.amount} | {expense.date}")
   
    def category_summary(self):
        if not self.collection:
           print("No expenses recorded.")
           return

        # Convert list of Expense objects to a pandas DataFrame
        data = {
            'Category': [e.category for e in self.collection],
            'Amount': [e.amount for e in self.collection]
        }
    
        df = pd.DataFrame(data)
    
        # Group by category and sum the amount
        summary = df.groupby('Category')['Amount'].sum().reset_index()
    
        # Print the summary
        print("\nTotal Spent Per Category:")
        for idx, row in summary.iterrows():
           print(f"{row['Category']}: {row['Amount']}")

   
    def save_to_csv(self, filename):
        if not self.collection:
            print("No expenses recorded to save.")
            return

         # Convert list of Expense objects to a pandas DataFrame
        data = {
              'Category': [e.category for e in self.collection],
              'Amount': [e.amount for e in self.collection],
               'Date': [e.date for e in self.collection]
        }
    
        df = pd.DataFrame(data)
    
         # Save DataFrame to CSV
        df.to_csv(filename, index=False)
        print(f"Expenses successfully saved to {filename}")

    def load_from_csv(self, filename):
        try:
           df = pd.read_csv(filename)

           if self.collection:
              confirm = input("This will overwrite current data. Continue? (y/n): ")
              if confirm.lower() != 'y':
                print("Load cancelled.")
                return

          # Clear current collection first, or append if you prefer
           self.collection.clear()

           for _, row in df.iterrows():
              expense = Expense(row['Category'], float(row['Amount']), row['Date'])
              self.collection.append(expense)

              print(f"Expenses successfully loaded from {filename}")

        except FileNotFoundError:
          print("File not found. Please make sure the file exists.")
        except Exception as e:
          print(f"An error occurred while loading the file: {e}")


def main():
    manager = ExpenseManager()
    while True:
        print("\n Menu :")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Show total spent per category")
        print("4. Save to CSV")
        print("5. Load from CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
             # Add a expense 
            category = input("Enter category: ")
            amount = float(input("Enter the amount: "))
            date = input("Enterthe date: ")
            new_expense = Expense (category , amount, date)
            manager.add_expense(new_expense)
            print(f"This '{category}' added to the expense.")
       
        elif choice == "2":
            manager.view_expenses()
        elif choice == "3":
            manager.category_summary()
        elif choice == "4":
            filename = input("Enter the filename to save to (e.g., expenses.csv): ")
            manager.save_to_csv(filename)
        elif choice == "5":
             filename = input("Enter the filename to load from (e.g., expenses.csv): ")
             manager.load_from_csv(filename)
        elif choice == "6":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 6.")

# Start the program
main()
