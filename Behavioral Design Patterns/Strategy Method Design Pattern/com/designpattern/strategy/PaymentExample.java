package com.designpattern.strategy;

public class PaymentExample
{
    public static void main(String[] args)
    {
        ShoppingCart cart = new ShoppingCart();

        // Pay with Credit Card
        cart.setPaymentStrategy(new CreditCardPayment("1234-5678-9012-3456", "John Doe"));
        cart.checkout(100);

        // Pay with PayPal
        cart.setPaymentStrategy(new PayPalPayment("john@example.com"));
        cart.checkout(200);

        // Pay with Cryptocurrency
        cart.setPaymentStrategy(new CryptoCurrencyPayment("crypto-wallet-123"));
        cart.checkout(300);
    }
}
