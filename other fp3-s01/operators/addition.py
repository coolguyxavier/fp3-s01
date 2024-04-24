# - FP3-S01 Libraries and Modules / Addition Calulator - #
# - Xzavier Moosomin - #
# - 04/24/2024 - #


# - Developer Notes - #
# THIS FILE SHOULD NOT BE USED ALONE
# THIS IS FOR THE ADDITION PART OF THE CALCULATOR


# - Functions - #

def add(dicts):
    num1 = float(input("What do you want your 1st number to be?\n>"))
    num2 = float(input("What do you want your 2nd number to be?\n>"))
   
    sum1 = num1 + num2
   
    dicts["Previous Answer(1)"] = sum1
    return sum1

# - Code - #
