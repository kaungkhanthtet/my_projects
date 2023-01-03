
# Way 1: without Function

num_one = float(input('First number:'), )
op = input('Operator:')
num_two = float(input('Second number:'))


if op == "+":   
    print("Result =",  num_one + num_two)

elif op == "-":
     print("Result =",  num_one - num_two)

elif op == "/":
    if num_two != 0:
        print("Result =",  num_one / num_two)
    else:
        print ("Zero Division Error!")
      
else :
     print("Result =",  num_one * num_two)

print("**********")

# Way 2: With Function

def add(num1, num2):
    return(num1+num2)

def sub(num1, num2):
    return(num1-num2)

def multi(num1, num2):
    return(num1*num2)

def div(num1, num2):
    return(num1/num2)
    
num1 = float(input("First number:"))
op = input("Operator:")
num2 = float(input("Second number:"))

if op == "+":
    print("Result =", add(num1, num2))

if op == "-":
    print("Result =", sub(num1, num2))

if op == "*":
    print("Result =", multi(num1, num2))

if op == "/":
    if num2 == 0:
       print("Zero Division Error!")
    else:
       print("Result =", div(num1, num2))

print("**********")

