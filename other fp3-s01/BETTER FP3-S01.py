# - FP3-S01 Libraries and Modules - #
# - Xzavier Moosomin - #
# - 04/24/2024 - #


# - Developer Notes - #
# this was a second shot since i didnt like the other one
# 5 minute coding adventure
# basic calculator, with the ability to remember past answers
# shouldn't require a dictionary, but i can figure it out

# - Imports - #
from operators import addition
from operators import subtraction
from operators import multiplication
from operators import division
from time import sleep

# - Dictionaries - #

prevans = { }

# - Functions - #


# - Variables - #
run = 1

# - Main Code - #

print("Here we go. Simple Calculator using modules.")
sleep(1)
print("It's like a better version of the Math Module.")
sleep(1)
print("By the way, you can only see your previous answer.")
sleep(1)
print("Any more than that and it'll be too overpowered.")
sleep(1)

while run == 1:
    if len(prevans) > 1:
        del prevans[0] # if there is already 2 answers stored and a third is being added,
        # it removes the first ordered element
   
    userchoice = input("""
What do you want to do?
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Quit
>""").lower()
   
    if userchoice == "1" or userchoice == "add":
        ans = addition.add(prevans) # passes the list into the function so it can append values
        print("Your answer is:", ans)
        print("Your previous answer(s) are:", prevans)
       
    elif userchoice == "2" or userchoice == "subtract":
        ans = subtraction.subtract(prevans)
        print("Your answer is:", ans)
        print("Your previous answer(s) are:", prevans)
       
    elif userchoice == "3" or userchoice == "multiply":
        ans = multiplication.multiply(prevans)
        print("Your answer is:", ans)
        print("Your previous answer(s) are:", prevans)
       
    elif userchoice == "4" or userchoice == "divide":
        ans = division.divide(prevans)
        print("Your answer is:", ans)
        print("Your previous answer(s) are:", prevans)
       
    elif userchoice == "5" or userchoice == "quit":
        run = 0
       
print("Bye bye!")

