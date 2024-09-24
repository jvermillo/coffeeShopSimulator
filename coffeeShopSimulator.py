# Juniper Vermillo
# CIS 129
# 9/23/2024
# coffeeShopSimulator.py 
'''This asks the user how many coffees and muffins they want, then calculates the total they'll pay based on it'''

print('Welcome to Marshmallow Cat Cafe! A cafe for all things sweet and tight-knit \n')

# Quantity of Items
coffeeCount = int(input('How many coffees will you be having? Coffee is $5 each '))
muffinCount = int(input('And how many muffins do you want? Muffins are $4 each '))

# Total Price
total = round(((coffeeCount + muffinCount) * 1.06), 2)
print('The total will be', str(total) + '.')