# Ask user to enter values for num_watermelons and cash_in_hand
num_watermelons = int(input("How many watermelons do you want to buy?: "))
cash_in_hand = int(input("How much money do you have?: "))

# Prompt user to buy at least 4 watermelons
if num_watermelons < 4:
    print('Please purchase at least 4 watermelons.')
# See if the user has enough money
else:
    total_cost = num_watermelons * 4
    if total_cost <= cash_in_hand:
        print('Approved transaction')
    else:
        print('You need more money to purchase all of the watermelons!')