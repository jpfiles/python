# Write a program that takes in an integer in the range 11-99 (inclusive) as 
# input. The output of the program is a countdown starting from the input 
# integer until an integer where both digits are identical.

# Ex: If the input is:
# 93

# the output is:
# 93
# 92
# 91
# 90
# 89
# 88

# Ex: If the input is:
# 11 or 99
# the output is:
# 11 or 99 respectively.

# Ex: If the input is:
# 9
# or any value not between 11 and 99 (inclusive), the output is:
# Input must be 11-99
# Use a while loop. Compare the digits; do not write a large if-else for all 
# possible same-digit numbers (11, 22, 33, â¦, 99), as that approach would be 
# cumbersome for larger ranges.

def countdown_with_same_digits(start):
    if not (11 <= start <= 99):
        return "Input must be 11-99"

    while True:
        tens = start // 10  # Get the tens digit
        ones = start % 10   # Get the ones digit
        print(start)
        if tens == ones:    # If the digits are the same, stop
            break
        start -= 1          # Decrement the number

# Example usage:
number = int(input("Enter a number between 11 and 99: "))
result = countdown_with_same_digits(number)
if result:
    print(result)
