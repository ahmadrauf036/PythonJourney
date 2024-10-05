name=input("Enter your  name: ")
#in operator
if(len(name)<10):
    print("less then 10")
else: 
    print("bigger than 10")
l=["ali","ahmad","salman","mohsin"]
if name in l:
    print("present")
else:
    print("absent")
    