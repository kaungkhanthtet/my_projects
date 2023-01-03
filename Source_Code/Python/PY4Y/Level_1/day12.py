magicians = ["Harry Potter", "Harmony", "Ron Wisley"]
for magician in magicians:
    print(magician)

print('**********')

my_list = [3, 5.0, "Python"]
for each_item in my_list:
    print(each_item)

print('**********')

names = ["Nathan", "Sai Win Naing", "Kaung Khant Htet", "Htet Wai Yan Aung"]

for each_one in names:
    print("Hello,", each_one +", nice to meet you!")

print('**********')

a = 20
b = 10
print(a < b)
print(a > b)
print(a > 10 and b == 10)
print(a <= 20 or b > 10)
print(not a >= 20)

print('**********')

nums = [1,3,2,5,6,79,46,13,56,99,19,16,38]

even = []
odd = []

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers =", even)
print("Odd numbers =", odd)

print('**********')

num = 4

if num%2 == 0:
    print(num, "is even number")
elif num%3 == 0:
    print(num, "is divisible by 3")
else:
    print(num, "is odd number")

print('**********')

i = 0

while i<5:
    print(i)
    i += 1

print('**********')

i = 1

while i <= 10:
    print(i)
    i+=1

print('**********')

name_list = []
num = 0
while num <  5:
    name_list.append("Kaung Khant Htet")
    num += 1

print(name_list)

print('**********')

def myself ():
    print("My name is Kaung khant Htet.", "I'm 14 years old and a student of LTE.")

myself()

print('**********')

def area_of_square (a1, a2):
    print (a1 * a2)

area_of_square(3, 3)

print('**********')

