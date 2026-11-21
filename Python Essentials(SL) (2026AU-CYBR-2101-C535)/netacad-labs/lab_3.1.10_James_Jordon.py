#Starts with the name of the plant 
plant_name = input("Enter the name of the plant: ")
print("The name of the plant is:", plant_name)

if plant_name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant_name}!")