
# ==========================================
# PROJECT PHARAOH: Pyramid Construction
# Mission: Build a monument worthy of Egypt.
# Budget: Whatever blocks we have left.
# ==========================================

blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 1

# Initiate pyramid construction protocol.
while blocks >= layer:

    # Deduct construction materials.
    blocks -= layer

    # Record the completed layer.
    height += 1

    # Calculate the next layer's requirements.
    layer += 1

# Report the final construction height.
print("The height of the pyramid:", height)
