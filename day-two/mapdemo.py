listx=[34,353,534,344,53,43,356,34,354,6,34,53,5,35,34,534]

def examine(x):
    if (x%2==0):
        return "Even"
    else:
        return "Odd"

result =map(examine,listx)
print(listx)
print(list(result))

result2 =map(lambda x: "Even" if (x%2==0) else "Odd",listx)
print(list(result2))