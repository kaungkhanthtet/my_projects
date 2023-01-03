day = eval(input("What is your Day of Birth : "))
month = eval(input("What is your Month of Birth : "))
year = eval(input("What is your Year of Birth : "))
Obj = day+month+year
obj_1= Obj%7

ze = 'You will be a father in 2050!'
one = 'You will have a great career in 2024!'
two = 'You will become rich in 2023!'
thr = 'Lottery Winnner of 2023!'
four = 'Lambogini owner in 2025!'
five = 'Three trillion dollars\' man!'
six = 'You will die in 3000!'

if obj_1 == 0:
    print('Your future is :', ze)
elif obj_1 == 1:
    print('Your future is :', one)
elif obj_1 == 2:
    print('Your future is :', two)
elif obj_1 == 3:
    print('Your future is', thr)
elif obj_1 == 4:
    print('Your future is :', four)
elif obj_1 == 5:
    print('Your future is :', five)
elif obj_1 == 6:
    print('Your future is :', six)