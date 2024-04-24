# - FP3-S01 Libraries and Modules / Division Calulator - #
# - Xzavier Moosomin - #
# - 04/24/2024 - #


# - Developer Notes - #
# THIS FILE SHOULD NOT BE USED ALONE
# THIS IS FOR THE DIVISION PART OF THE CALCULATOR


# - Functions - #

def divide(dicts):
    num1 = float(input("What do you want your 1st number to be?\n>"))
    num2 = float(input("What do you want your 2nd number to be?\n>"))
   
    quotient = num1 / num2
   
    dicts["Previous Answer(1)"] = quotient
   
    return quotient


# - Code - #
