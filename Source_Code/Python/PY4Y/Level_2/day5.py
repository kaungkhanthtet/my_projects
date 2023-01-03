#No parameter

def greet():
    print("Hello, my name is Kaung Khant Htet")

greet()

#Parameter

def greet(name): #Function's parameter
    print("Hello, my name is", name)

greet("Kaung Khant Htet") #Function's argument

print("**********")
#More than one parameters

def add_two_numbers(a,b):
    print(a+b)

add_two_numbers(5,6)

print("**********")
#Using Return keyword
#Store and Use the Return value

def sub_two_numbers(a,b):
    subtraction = a - b
    return subtraction

result = sub_two_numbers(20,10)
print(result)

print("**********")
#Exercise

def oddCount(num_list):
    count = 0
    for i in num_list:
        if i%2 != 0:
            count += 1
    return count

nums = [1, 2, 3, 4, 5, 6]
result = oddCount(nums)
print("The number of odd numbers in the list :", result)

print("**********")

