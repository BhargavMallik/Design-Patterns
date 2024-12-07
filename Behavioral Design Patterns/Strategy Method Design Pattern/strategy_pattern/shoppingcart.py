from strategy_pattern.creditcard_payment import CreditCardPayment
from strategy_pattern.cryptocurrency_payment import CryptoCurrencyPayment
from strategy_pattern.paypal_payment import PayPalPayment

# Context
class ShoppingCart:
    def __init__(self):
        self.payment_strategy = None

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


# Client Code
if __name__ == "__main__":
    cart = ShoppingCart()

    # Pay with Credit Card
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "John Doe"))
    cart.checkout(100)

    # Pay with PayPal
    cart.set_payment_strategy(PayPalPayment("john@example.com"))
    cart.checkout(200)

    # Pay with Cryptocurrency
    cart.set_payment_strategy(CryptoCurrencyPayment("crypto-wallet-123"))
    cart.checkout(300)
