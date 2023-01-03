# print("\"Python!\"" )

# print("**********")

# print("Here is \na sentence \non many \ndifferent lines")

# print("**********")

# print("\tHello World")
# print("Hello World\t")
# print("Hello \tWorld")

# print("**********")

# #Exercise
# print("Which one of these is a fish? \nA) Whale \nB) Dolphin \nC) Shark \nD) Squid \nType A, B, C, or D")

# print("**********")

# name = input("What is your name?")
# age = input("How old are you?")
# print("Name :", name)
# print("Age :", age)

# print("**********")

# num_one = input("Enter your first number:")
# num_two = input("Enter the second number:")
# total = num_one + num_two
# print("Total is", total)

# num_one = input("Enter your first number:")
# num_two = input("Enter the second number:")
# total = float(num_one) + float(num_two)
# print("Total is", total)

# print("**********")

# age = 14
# to_print = "I am " + str(age) + " years old."
# print(to_print)

# 
print("**********")
#Exercise 1

ans = input("Which one of these is not a fish? \nA) Whale \nB) Dolphin \nC) Shark \nD) Squid \nType A, B, C, or D :")

if ans == "D" or "d":
    print("Your answer \""+ans.upper()+"\" is correct!")
else:
    print(ans.upper(),"is incorrect. Try Again!")

print("**********")

num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number:"))
con = input("Press A to Add or Press M to Multiply:")

if con == "A"or"a":
    result = num_1 + num_2
elif con == "M"or"m":
    result = num_1 * num_2
else:
    print("Out of data, Try Again!")

print(result)

print("**********")