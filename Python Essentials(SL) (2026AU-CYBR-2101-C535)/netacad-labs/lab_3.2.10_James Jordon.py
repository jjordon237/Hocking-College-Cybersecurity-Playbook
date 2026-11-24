# Project Chupacabra II: The Ugly Vowel Eater
# Mission: Eliminate all vowels.
user_word = input("Enter a word: ")
user_word = user_word.upper()

#Looks through each letter in the user_word variable for vowels TO EAT!
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter, end="")
