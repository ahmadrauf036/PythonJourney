#operators, escape characters and use of print and input

#input returns a string value

#get an input as int
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

#adding 2 numbers
print("Sum is: ",a+b,"\n")

#mod operator
a=int(input("Enter a number: "))
b=int(input("Enter a divisor: "))

print("Remainder is: ",a%b,"\n")

#datatypes
c=input("Enter: ")
print("Type: ",type(c),"\n")
d=9
print("Type: ",type(d),"\n")
e=9.5
print("Type: ",type(e),"\n")

#relational operators
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

if a==b:
    print("both are equal","\n")
elif a>b:
    print("a is greater than b","\n")
else:
    print("b is greater than a"),"\n"

#some other operators
print("Average = ",(a+b)/2,"\n")
print("Square of number 1 = ",a**2,"\n")
print("cube of number 2 = ",b**3,"\n")


input("Press Enter to continue...")