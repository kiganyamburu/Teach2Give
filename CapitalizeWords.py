# Write a program that accepts a string as input, 
# capitalizes the first letter of each word in the string, 
# and then returns the result string.

def capitalize_first_letter(input_string):
    words = input_string.split() 
    capitalized_words = [word.capitalize() for word in words]  
    result_string = ' '.join(capitalized_words)  
    return result_string

user_input = input("Enter a string: ")
result = capitalize_first_letter(user_input)

print(f"Original string: {user_input}")
print(f"Capitalized string: {result}")
