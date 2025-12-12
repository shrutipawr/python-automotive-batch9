def calc(a,b,op):   
    if op == '+':return a+b
    if op == '-':return a-b
    if op == '*':return a*b
    if op == '/':return a/b

a=int(input("Enter first number: "))   
b=int(input("Enter second number: ")) 
op=input("Enter operator(+,-,*,/): ")
print("Result: ", calc(a, b, op))  