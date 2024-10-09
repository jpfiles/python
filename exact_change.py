# Define a function called exact_change that takes the total change amount in cents and calculates the change using the fewest coins. The coin types are pennies, nickels, dimes, and quarters. Then write a main program that reads the total change amount as an integer input, calls exact_change(), and outputs the change, one coin type per line. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies. Output "no change" if the input is 0 or less.

# Ex: If the input is:
# 0 
# (or less), the output is:
# no change

# Ex: If the input is:
# 45
# the output is:
# 2 dimes 
# 1 quarter

# Your program must define and call the following function. The function exact_change() should return a tuple containing num_pennies, num_nickels, num_dimes, and num_quarters.
# def exact_change(user_total)

def exact_change(user_total):
    quarters = user_total // 25
    user_total %= 25
    
    dimes = user_total // 10
    user_total %= 10
    
    nickels = user_total // 5
    user_total %= 5
    
    pennies = user_total
    
    return (pennies, nickels, dimes, quarters)

def main():
    total_cents = int(input('Input number 0 to 100: '))
    
    if total_cents <= 0:
        print("no change")
    else:
        pennies, nickels, dimes, quarters = exact_change(total_cents)
        if pennies > 0:
            print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}") 
        if nickels > 0:
            print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
        if dimes > 0:
            print(f"{dimes} dime{'s' if dimes > 1 else ''}") 
        if quarters > 0:
            print(f"{quarters} quarter{'s' if quarters > 1 else ''}")  

if __name__ == "__main__":
    main()