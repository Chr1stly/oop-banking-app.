class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner.strip().title()
        self.balance = initial_balance
        self.loan_balance = 0.0
        self.daily_withdrawal_limit = 150000.0
        self.max_loan_limit = 300000.0

    def print_divider(self):
        print("*" * 30)

    def show_balance(self):
        self.print_divider()
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: N{self.balance:,.2f}")
        if self.loan_balance > 0:
            print(f"Outstanding Loan: N{self.loan_balance:,.2f}")
        self.print_divider()

    def deposit(self):
        try:
            amount = float(input("Enter an Amount to Deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            self.balance += amount
            self.print_divider()
            print(f"Successfully deposited N{amount:,.2f} into your account.")
            self.print_divider()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter Amount to Withdraw: "))
            self.print_divider()

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient Balance.")
            elif amount > self.daily_withdrawal_limit:
                print(f"Limit exceeded! Maximum daily withdrawal is N{self.daily_withdrawal_limit:,.2f}")
            else:
                self.balance -= amount
                print(f"Successfully withdrew N{amount:,.2f} from your account.")
            self.print_divider()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def buy_airtime(self):
        network = input("Select network (MTN, AIRTEL, 9MOBILE, GLO): ").upper()
        try:
            amount = float(input("Enter airtime amount: "))
            if amount <= 0:
                print("Invalid amount.")
                return

            phone_number = input("Enter 11-digit phone number: ").strip()
            if not phone_number.isdigit() or len(phone_number) != 11:
                print("Invalid phone number. Must be exactly 11 digits.")
                return

            if amount > self.balance:
                print("Insufficient Balance.")
            else:
                self.balance -= amount
                self.print_divider()
                print(f"Successfully purchased N{amount:,.2f} airtime for {phone_number} on {network}.")
                self.print_divider()
        except ValueError:
            print("Invalid numerical input.")

    def apply_loan(self):
        try:
            amount = float(input(f"Enter loan amount (Max N{self.max_loan_limit:,.2f}): "))
            self.print_divider()

            if amount <= 0:
                print("Loan amount must be positive.")
            elif amount > self.max_loan_limit:
                print("Loan request exceeds maximum allowed limit.")
            elif self.loan_balance > 0:
                print("You must clear your outstanding loan before requesting a new one.")
            else:
                self.loan_balance += amount
                self.balance += amount
                print(f"Loan of N{amount:,.2f} approved and added to your balance.")
            self.print_divider()
        except ValueError:
            print("Invalid input.")

    def invest(self):
        try:
            principal = float(input("Enter amount to invest: "))
            if principal <= 0 or principal > self.balance:
                print("Invalid amount or insufficient balance.")
                return

            rate = float(input("Enter annual interest rate (in %): "))
            time = float(input("Enter investment duration (in years): "))

            interest = (principal * rate * time) / 100
            total_return = principal + interest

            self.balance -= principal

            self.print_divider()
            print(f"Invested N{principal:,.2f} at {rate}% for {time} years.")
            print(f"Projected Interest: N{interest:,.2f}")
            print(f"Total Return upon maturity: N{total_return:,.2f}")
            self.print_divider()
        except ValueError:
            print("Invalid inputs. Please try again.")


def main():
    name = input("Welcome to C's Bank PLC. Please enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nWhat would you like to do today?")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Show Balance")
        print("4. Buy Airtime")
        print("5. Get a Loan")
        print("6. Invest")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        match choice:
            case '1':
                account.deposit()
            case '2':
                account.withdraw()
            case '3':
                account.show_balance()
            case '4':
                account.buy_airtime()
            case '5':
                account.apply_loan()
            case '6':
                account.invest()
            case '7':
                print("\nThank you for banking with us!")
                break
            case _:
                print("Invalid option chosen. Please select 1-7.")


if __name__ == "__main__":
    main()