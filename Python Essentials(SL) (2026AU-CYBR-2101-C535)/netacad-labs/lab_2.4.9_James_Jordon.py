kilometers = 119965.42
miles = 985673.99

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

LIRE = 1000000
USD = 100

#Historical Exchange Rate (1996): 1 Lira = 0.00064813 USD
exchange_rate = 1542.90

LIRE_to_USD = LIRE / exchange_rate
USD_to_LIRE = USD * exchange_rate 

print(LIRE, "1996 Italian LIRE is", round(LIRE_to_USD, 2), "USD")
print(USD, "1996 USD is", round(USD_to_LIRE, 2), "LIRE")
