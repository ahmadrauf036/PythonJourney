#factorial

num=int(input("Enter number: "))
temp=num
fact=1
while temp>1:
    fact*=temp
    temp-=1
print(f"Factorial: {fact}")
