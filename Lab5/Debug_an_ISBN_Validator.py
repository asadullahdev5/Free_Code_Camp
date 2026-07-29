# Debug an ISBN Validator
# The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits.

# Camperbot has tried to build their own ISBN validator. However, they have made a few mistakes along the way.

# In this lab, you will fix the existing code and make it function properly.

# Expected behavior: When the user runs the program, it will show the prompt Enter ISBN and length: . The user can enter the ISBN code they want to validate in ISBN,length format. The ISBN code should not contain hyphens, followed by its length (10 or 13), separated by a comma.

# Example inputs: 1530051126,10 for ISBN-10 codes. 9781530051120,13 for ISBN-13 codes.

# How to find the check digit:

# You don't have to know the detailed calculation logic in this lab. The functions calculate_check_digit_10 and calculate_check_digit_13 will take care of the calculation and return the expected check digit in string.
# The check digit for ISBN-10 codes can be a number from 0 to 9 or an uppercase letter X.
# The check digit for ISBN-13 codes can be a number from 0 to 9.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should fix the IndentationError in the current code.
# Even if the user does not enter a comma separated value, the program should handle the IndexError without crashing.
# When the user does not enter a comma separated value, they should see the message Enter comma-separated values. in the console, and the program should terminate.
# Even if the user enters a non-numeric value for the length, the program should handle the ValueError without crashing.
# When the user enters a non-numeric value for the length, they should see the message Length must be a number. in the console, and the program should terminate.
# You should fix the off-by-one error in the validate_isbn function.
# You should fix the TypeError in the current code that occurs when the user enters a valid ISBN code.
# You should fix the IndexError in the current code when the user enters a valid ISBN code.
# Even if the user enters an incorrect ISBN code with characters other than numbers, the program should handle the ValueError that occurs without crashing.
# When the user enters an incorrect ISBN code with characters other than numbers, they should see the message Invalid character was found. in the console.
# When the user enters 1530051126,10, they should see the message Valid ISBN Code.
# When the user enters 9781530051120,13, they should see the message Valid ISBN Code.
# Important: you will need to comment out the main() call in the global space for the tests to run properly.

# When you complete the project, the user should see the message Valid ISBN Code. when they enter a valid ISBN code, and Invalid ISBN Code. when they enter an invalid ISBN code.





def validate_isbn(isbn, length):
    # Separate the first (length - 1) digits from the final check digit
    main_digits = isbn[0:length-1]
    given_check_digit = isbn[-1].upper()  # Ensure 'x' becomes 'X'
    
    # Convert only the main digits to integers
    main_digits_list = [int(digit) for digit in main_digits]
    
    # Calculate the expected check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
        
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2)
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
        
    result = 11 - digits_sum % 11
    
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1)
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
            
    result = 10 - digits_sum % 10
    
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main(): 
    user_input = input('Enter ISBN and length: ') 
    
    if ',' not in user_input: 
        print("Enter comma-separated values.") 
        return 
        
    values = user_input.split(',') 
    isbn = values[0].strip() 
    length_str = values[1].strip()
    
    if not length_str.isdigit(): 
        print("Length must be a number.") 
        return 
        
    length = int(length_str)
    
    if length == 10 or length == 13: 
        # Verify requested length matches provided code length
        if length == 10 and len(isbn) != 10:
            print("ISBN-10 code should be 10 digits long.")
            return

        if length == 13 and len(isbn) != 13:
            print("ISBN-13 code should be 13 digits long.")
            return

        # Rule 8: Character validation
        is_valid_chars = isbn.isdigit() or (length == 10 and isbn[:-1].isdigit() and isbn[-1].upper() == 'X')
        
        if not is_valid_chars:
            print("Invalid character was found.")
            return
            
        # Safely run validation calculations
        validate_isbn(isbn, length) 
    else: 
        print('Length should be 10 or 13.')
