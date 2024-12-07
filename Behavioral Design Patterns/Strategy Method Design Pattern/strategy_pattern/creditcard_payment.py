from strategy_pattern.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name

    def pay(self, amount):
        print(f"{amount} paid using Credit Card")