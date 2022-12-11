import json


coins = [
    {
        "symbol" : "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
    },
    {
        "symbol": "BTS",
        "amount_owned": 4,
        "price_per_coin": 6200
    }
]

for coin in coins:
    print(coin["price_per_coin"])

