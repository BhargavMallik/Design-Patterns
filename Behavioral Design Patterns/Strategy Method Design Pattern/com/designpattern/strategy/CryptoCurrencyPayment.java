package com.designpattern.strategy;

public class CryptoCurrencyPayment implements PaymentStrategy
{
    private String walletId;

    public CryptoCurrencyPayment(String walletId)
    {
        this.walletId = walletId;
    }

    @Override
    public void pay(int amount)
    {
        System.out.println(amount + " paid using Cryptocurrency");
    }
}
