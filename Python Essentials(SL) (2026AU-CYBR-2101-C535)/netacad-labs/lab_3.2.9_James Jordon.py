print("========================================")
print("       PROJECT CHUPACABRA - AVMC")
print("       CLASSIFIED SECURITY TERMINAL")
print("========================================")
print("Security lockdown initiated.")
print("Even the coffee machine is classified.")
print()

while True:
    word = input("Enter emergency override code: ")

    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    else:
        print("ACCESS DENIED. Nice try, human.")
        continue