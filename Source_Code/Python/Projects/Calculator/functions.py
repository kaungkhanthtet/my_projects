def Calculate (a,b):
    def add(a, b):
        return(a+b)

    def sub(a, b):
        return(a-b)

    def multi(a, b):
        return(a*b)

    def div(a, b):
        return(a/b)
        
    if op == "+":
        print("Result =", add(a, b))

    if op == "-":
        print("Result =", sub(a, b))

    if op == "*":
        print("Result =", multi(a, b))

    if op == "/":
        if b == 0:
        print("Zero Division Error!")
        else:
        print("Result =", div(a, b))