#sum of natural numbers with loops

num=int(input("Enter Number: "))
temp=num
sum=0
while temp:
    sum=temp+sum
    temp-=1
print(f"Sum: {sum}")