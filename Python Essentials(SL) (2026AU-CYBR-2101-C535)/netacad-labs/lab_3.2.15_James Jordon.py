# ==========================================
# PROJECT COLLATZ: Operation 3X+1
# The 1937 Mathematical Enigma
# Mission: Navigate the numerical chaos.
# Objective: Reach 1.
# ==========================================

c0 = int(input("Enter a positive integer: "))
steps = 0

# Initiate the Collatz sequence.
while c0 != 1:

    # Even number protocol.
    if c0 % 2 == 0:
        c0 = c0 // 2

    # Odd number protocol.
    else:
        c0 = 3 * c0 + 1

    # Record each mathematical maneuver.
    steps += 1
    print(c0)

# Final mission report.
print("steps =", steps)
