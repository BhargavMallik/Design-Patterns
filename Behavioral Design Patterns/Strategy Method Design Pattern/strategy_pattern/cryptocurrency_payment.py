from strategy_pattern.payment_strategy import PaymentStrategy

class CryptoCurrencyPayment(PaymentStrategy):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def pay(self, amount):
        print(f"{amount} paid using Cryptocurrency")