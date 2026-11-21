income = float(input("Enter the annual income: "))

if income <= 1000:
    tax = 0

#
elif income < 85528:
    tax = income * 0.18 - 556.02

#Income == 85528:
else:
    tax = 14839.02 + 0.32 * (income - 85528)

#I used a float instead of a round function due to
#the fact that the tax is already rounded to two decimal places in the formula. 
#This would be typoical of any tax calculation, as the tax is calculated to the nearest cent.
print("The tax is:", float(tax), "thalers")
 