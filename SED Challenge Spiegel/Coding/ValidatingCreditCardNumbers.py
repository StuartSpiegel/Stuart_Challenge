# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.

# Examples:

# Valid Credit Card Numbers

# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
# Invalid Credit Card Numbers

# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
# Input Format

# The first line of input contains an integer .
# The next  lines contain credit card numbers.

# Constraints


# Output Format

# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

# Regular expressions library
import re

input_file = open("input.txt", "r") # open the file for reading
# for current index (Credit card entry) in the list of all entries (input)
for _ in input_file.readlines():
    num = _ # the current inspected element is fed in from the input
#     It must start with a 4,5,or 6 .
# ►   It must contain exactly 16 digits.
    check1 = bool(re.match(r"^[456]\d{15}$", num)) # First conditional check
    
    # It may have digits in groups of 4 , separated by one hyphen "-".
    check2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "") # Hyphens are ok
    
    # It must NOT have 4 or more consecutive repeated digits.
    check3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (check1 or check2) and check3:
        print("Valid")
    else:
        print("Invalid")