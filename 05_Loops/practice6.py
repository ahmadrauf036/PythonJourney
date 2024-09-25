#multiplication table in reverse order

num=int(input("Enter number: "))
 
for i in range(10,0,-1):
    print(f"{num} * {i} = {num*i}")
