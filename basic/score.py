def score(m):
    if m > 60:
        return "Pass"
    else:
        return "Fail"
n=int(input("Enter Physics marks: "))
print("Result: ", score(n))    