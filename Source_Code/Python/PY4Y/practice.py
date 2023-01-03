# nums = [ 1, 2, 3, 4, 5, 11, 16, 100, 99, 58, 69, 78, 199]

# even = []
# odd = []
# outlier = []

# for i in nums:
    
#     if i>90:
#         outlier.append(i)
#     elif i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers =", even)
# print("Odd numbers =", odd)
# print("Outlier numbers =", outlier)

# print('**********')

# num_1 = int(input("number one:"))
# unchanged_num = 2
# result = num_1%2

# if result is 0:
#     print("It is even number")
    
# else:
#     print("It is odd number")

# print('**********')

# num_1 = int(input("Your number:"))

# if num_1%2 == 0:
#  print(num_1, "is even number")

# elif num_1%3 == 0:
#  print(num_1, "is divisible with 3")

# else:
#   print(num_1, "is odd number")
  
# print("**********")

# def CheckLeap(Year):
#     if ((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0) and not (Year % 4 != 0)):
#         print("Given year is a leap year!")

#     else:
#         print("Given year is not a leap year!")

# Year = int(input('Enter the year:'))

# CheckLeap(Year)

# print("**********")

txt = str(input("Enter the phrase:"))
sch = str(input("Enter the word what u want to search:"))

if sch in txt:
    print(sch, "is included in your phrase")
else:
    print("Sorry,", sch, "is not included in your phrase")

print("**********")


