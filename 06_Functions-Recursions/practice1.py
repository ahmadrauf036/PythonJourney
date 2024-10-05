# creating a function

def greatestOf3(a:int,b:int,c:int):
    if (a>b) and (a>c):
        print(f"{a} is greater.")
    elif (b>a) and (b>c):
        print(f"{b} is greater.")
    elif (c>b) and (c>a):
        print(f"{c} is greater.")
    elif a==b==c:
        print("Equal values.")

def main():
    a=int(input("Enter 1st value: "))
    b=int(input("Enter 2nd value: "))
    c=int(input("Enter 3rd value: "))
    
    greatestOf3(a,b,c)
    
main()
        
        