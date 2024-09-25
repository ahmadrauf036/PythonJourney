#conditional statements

#greatest in 4 numbers

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
d=int(input("Enter 4th number: "))

if a==b and b==c and c==d:
    print("All numbers are equal.")
elif a>b and a>c and a>d:
    print(f"{a} is greater")
elif c>b and c>a and c>d:
    print(f"{c} is greater")
elif d>b and d>c and d>a:
    print(f"{d} is greater")
elif b>a and b>c and b>d:
    print(f"{b} is greater")
    
input("press enter to continue...")