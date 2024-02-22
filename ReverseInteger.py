# Write a program that takes an integer
# as input and returns an integer 
# with reversed digit ordering.
def reverse_digits(input_integer):
    
    reversed_str = str(input_integer)[::-1]
    reversed_integer = int(reversed_str)
    return reversed_integer

user_input = int(input("Enter an integer: "))
result = reverse_digits(user_input)

print(f"Original integer: {user_input}")
print(f"Integer with reversed digit ordering: {result}")
