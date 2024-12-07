from strategy_pattern.payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"{amount} paid using PayPal")