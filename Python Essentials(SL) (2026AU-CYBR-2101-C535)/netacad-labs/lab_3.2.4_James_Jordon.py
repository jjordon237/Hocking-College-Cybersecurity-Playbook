#$Secret number is 777
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter a three-digit number     |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Read the first guess.
while secret_number != 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
    
    else:
        print("Ha ha! You're stuck in my loop!")