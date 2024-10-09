# Write a program that reads a list of integers into a list as long as the 
# integers are greater than zero, then outputs the smallest and largest integers 
# in the list.

# Ex: If the input is:
# 10
# 5
# 3
# 21
# 2
# -6

# the output is:
# 2 and 21
# You can assume that the list of integers will have at least 2 values.

def read_integers():
    integers = []
    while True:
        number = int(input("Enter a positive integer (or a non-positive to stop): "))
        if number <= 0:
            break
        integers.append(number)

    if integers:  # Check if the list is not empty
        smallest = min(integers)
        largest = max(integers)
        print(f"{smallest} and {largest}")

# Example usage
read_integers()