exchange_rates = [
    {
        "ccy":"EUR",
        "base_ccy":"UAH",
        "buy":"47.99000",
        "sale":"48.99000"
        },

    {
        "ccy":"USD",
        "base_ccy":"UAH",
        "buy":"40.95000",
        "sale":"41.55000"}
     ]

def convert_currency():
    inputNumber = float(input("Введіть вашу стипендію (в гривнях): "))

    for rate in exchange_rates:
        currency = rate["ccy"]
        buy_rate = float(rate["buy"])
        
        result = inputNumber / buy_rate
        print(f"Ваша стипендія у {currency}: {round(result, 2)}")

convert_currency()