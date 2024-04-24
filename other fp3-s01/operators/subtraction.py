# - FP3-S01 Libraries and Modules / Subtraction Calulator - #
# - Xzavier Moosomin - #
# - 04/24/2024 - #


# - Developer Notes - #
# THIS FILE SHOULD NOT BE USED ALONE
# THIS IS FOR THE SUBTRACTION PART OF THE CALCULATOR


# - Functions - #

def subtract(dicts):
    num1 = float(input("What do you want your 1st number to be?\n>"))
    num2 = float(input("What do you want your 2nd number to be?\n>"))
   
    difference = num1 - num2
   
    dicts["Previous Answer(1)"] = difference
   
    return difference
   
# - Code - #
