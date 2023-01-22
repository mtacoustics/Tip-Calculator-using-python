# Ask user for the total bill amount and store that in a variable
billTotal = input('What is the bill total? \n')

# Because this is usually a decimal convert str to a float
billTotal = float(billTotal)

# Ask user how large of a tip they want to leave
tipPercentage = input('How big of a tip would you like to leave? \n')

# Convert to an integer and turn percentage into decimal
tipPercentage = int(tipPercentage) / 100

# Formula that calculates tip
tipAmount = billTotal * tipPercentage

# Formula that calculates new total
newBillTotal = billTotal + tipAmount

# Print out tip amount and total for easy math for user
print("Please leave $" + str(round(tipAmount, 2)) + " as the tip.\nYour new total is $" + str(round(newBillTotal, 2)))
