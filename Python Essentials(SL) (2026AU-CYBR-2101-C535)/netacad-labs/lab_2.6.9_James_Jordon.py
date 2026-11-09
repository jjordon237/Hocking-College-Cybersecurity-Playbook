# 1996 Italian Lire to USD Converter (Historcal Exchange Rate)
#Includes a 3% conversion rate fee for converting Italian Lire to USD and 2.00 USD processing fee for each transaction.
exchange_rate = 1542.9
fee_rate = 0.03
processing_fee = 2.00

# Get user input and convert to float
A = float(input("Enter Italian Lire: "))
B = float(input("Enter US Dollars: "))

# Calculate conversions
lire_to_usd = A / exchange_rate
usd_to_lire = B * exchange_rate

#Calculate 3% conversion fee
usd_fee = lire_to_usd * fee_rate
lire_fee = usd_to_lire * fee_rate

#Subtract fees from converted amounts-currencies
final_usd = lire_to_usd - usd_fee
final_lire = usd_to_lire - lire_fee

# Convert processing fee to Italian Lire
lire_processing_fee = processing_fee * exchange_rate

#Add the processing fee for total fee amounts 
total_usd_fee = usd_fee + processing_fee
total_lire_fee = lire_fee + processing_fee
final_usd_after_processing = final_usd - total_usd_fee
final_lire_after_processing = final_lire - total_lire_fee

# Italian Lire to USD transaction
print(A, "Italian Lire is", round(lire_to_usd, 2), "USD")
print("USD before fees:", round(lire_to_usd, 2))
print("USD conversion fee:", round(usd_fee, 2))
print("USD processing fee:", round(processing_fee, 2))
print("Total USD fees:", round(total_usd_fee, 2))
print("USD after fees:", round(final_usd_after_processing, 2))

print()

# USD to Italian Lire transaction
print(B, "USD is", round(usd_to_lire, 2), "Italian Lire")
print("Lire before fees:", round(usd_to_lire, 2))
print("Lire conversion fee:", round(lire_fee, 2))
print("Lire processing fee:", round(lire_processing_fee, 2))
print("Total Lire fees:", round(total_lire_fee, 2))
print("Lire after fees:", round(final_lire_after_processing, 2))
print()

# Customer appreciation
print("Grazie per averci scelto!")

# My mother, older brother, and I travelled to Rome, Bari, and onto Croatia 
# to see my father in the UN. I have always wanted to complete this converter along with
# the fees that were added at the kiosk in the Rome airport. It shows conclusive 
# evidence of division, multiplication, addition and subtraction all in  a real-world application. 
# What currency, ficticious or real, would you like to see converted next? -1dleHand