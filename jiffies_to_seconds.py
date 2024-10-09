# In computer animation, a "jiffy" is commonly defined as 1/100th of a second. Define a function named jiffies_to_seconds that takes the number of "jiffies" as a parameter, and returns the number of seconds. Then, write a main program that reads the number of jiffies (float) as an input, calls function jiffies_to_seconds() with the input as argument, and outputs the number of seconds.

# Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.3f}')

# Ex: If the input is:
# 15.25

# the output is:
# 0.152

# The program must define and call the following function:
# def jiffies_to_seconds(user_jiffies)

def jiffies_to_seconds(user_jiffies):
    # Convert jiffies to seconds
    return user_jiffies / 100.0

if __name__ == '__main__':
    # Read input from the user
    user_input = float(input('Input a floating value: '))
    # Call the function and store the result
    seconds = jiffies_to_seconds(user_input)
    # Output the result formatted to three decimal places
    print(f'{seconds:.3f}')