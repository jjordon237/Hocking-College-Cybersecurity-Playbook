# ==========================================
# PROJECT CHUPACABRA III: Vowel_Eater_Boogaloo
# Mission: No vowel shall survive.
# Objective: Extract surviving consonants.
# ==========================================

#Vowel counter
word_without_vowels = ""
vowels_eaten = 0

#Chupacabra's vowel-eating loop
user_word = input("Chupacabra is Hungry! Feed the Chupacabra a word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter in "AEIOU":
        vowels_eaten += 1
        continue
    word_without_vowels += letter

print("Word without vowels:", word_without_vowels)
print("Number of vowels eaten:", vowels_eaten)