#prime or not

num=int(input("Enter number: "))

i=2
chk=False
while i<num:
    if num%i==0:
        print("non-prime")
        chk=True
        break
    i+=1
if not chk:
    print("prime")
    
    
