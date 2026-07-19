# Build an Apply Discount Function
# In this lab you will write a function that calculates the final price of an item after applying a percentage discount.
# For example, if the price of an item is 50 and a discount of 20 is applied, the discount amount is 10, and the final price is 40.
# Objective: Fulfill the user stories below to complete the lab.
# User Stories:
# You should define a function named apply_discount.
# The apply_discount function should take exactly two parameters: price and discount.
# If price is not a number (int or float), the function should return the string The price should be a number.
# If discount is not a number (int or float), the function should return the string The discount should be a number.
# If price is less than or equal to 0, the function should return the string The price should be greater than 0.
# If discount is less than 0 or greater than 100, the function should return the string The discount should be between 0 and 100.
# If both inputs are valid, the function should calculate the discount as a percentage of the price.
# The function should return the final price after applying the discount.


def apply_discount(price , discount):

    if not isinstance(price, (int, float)):
        return("The price should be a number")

    elif not isinstance(discount, (int, float)):
        return("The discount should be a number")
    
    if (price <= 0):
        return("The price should be greater than 0")

    elif (discount < 0) or (discount > 100):
        return("The discount should be between 0 and 100")
    else:
        return price - (price * discount / 100)
