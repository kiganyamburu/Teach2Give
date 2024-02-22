# Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = "aeiouAEIOU"  # Define a string of vowels
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

user_input = input("Enter a sentence: ")
result = count_vowels(user_input)

print(f"Number of vowels in the sentence: {result}")
