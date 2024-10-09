# Write a function driving_cost() with input parameters miles_per_gallon, 
# dollars_per_gallon, and miles_driven, that returns the dollar cost to drive 
# those miles. All items are of type float. The function called with arguments 
# (20.0, 3.1599, 50.0) returns 7.89975.

# Define that function in a program whose inputs are the car's miles per 
# gallon and the price of gas in dollars per gallon (both float). Output the 
# gas cost for 10 miles, 50 miles, and 400 miles, by calling your driving_cost() 
# function three times.

# Output each floating-point value with two digits after the decimal point, 
# which can be achieved as follows:
# print(f'{your_value:.2f}')

# Ex: If the input is:
# 20.0
# 3.1599

# the output is:
# 1.58
# 7.90
# 63.20

# Your program must define and call a function:
# def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)

# Function to calculate driving cost
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    # Input for miles per gallon and dollars per gallon
    miles_per_gallon = float(input("Enter the car's miles per gallon: "))
    dollars_per_gallon = float(input("Enter the price of gas per gallon: "))
    
    # Calculating costs for different distances
    cost_for_10_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
    cost_for_50_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
    cost_for_400_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)
    
    # Output the results formatted to two decimal places
    print(f'{cost_for_10_miles:.2f}')
    print(f'{cost_for_50_miles:.2f}')
    print(f'{cost_for_400_miles:.2f}')