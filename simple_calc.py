def calculate(a,b,op):
    if op =='+':
        return a+b
    elif op=='-':
        return a-b
    elif op == '*':
        return a*b
    elif op =='/':
        if b==0:
            return "Divsion by zero not possible"
        return a/b
    else:
        return "Invalid function"
    


