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

def convert_currency(amount, currency):
    for rate in exchange_rates:
        if rate["ccy"] == currency:
            return amount / float(rate["sale"])
        

inputUAH = float(input("Введіть суму в гривнях: "))
currency_code = input("Введіть валюту(EUR або USD): ")

result = convert_currency(inputUAH, currency_code)
print(f"Гривні в {currency_code}: {round(result, 2)}")



# def convert_currency():
#     for rate in exchange_rates:
#         currency = rate["ccy"]
#         buy_rate = float(rate["buy"])
        
#         result = inputNumber / buy_rate
#         print(f"Ваша стипендія у {currency}: {round(result, 2)}")

# convert_currency()