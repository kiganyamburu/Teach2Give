# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci_sequence(limit):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

limit = 100
result = fibonacci_sequence(limit)

print(f"Fibonacci sequence up to {limit}: {result}")
