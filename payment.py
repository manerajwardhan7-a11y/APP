class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


amount = float(input("Enter amount: "))

print("1. Credit Card")
print("2. UPI")
print("3. Cash")

choice = int(input("Select payment method: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = UPIPayment()
elif choice == 3:
    strategy = CashPayment()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)
