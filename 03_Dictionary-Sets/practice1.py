#creating dictionary

urdu={
    "how":"kese",
    "there":"wahan",
    "where":"kahan",
    "here":"yahan",
    "water":"pani",
    "bear":"sharab",
    "food":"khana",
    "is":"hai",
    "you":"tum"
}
print(urdu["water"],urdu["where"],urdu["is"],"?")

#dictionary functions
urdu.update({"is":"ho"})
print(urdu["you"],urdu["how"],urdu["is"],"?")

#Sets
#take unique values from user
s=set() #null set --> s={} this will make a null dictionary
print(type(s))
s.add(input("Enter number: "))
s.add(input("Enter number: "))
s.add(input("Enter number: "))
s.add(input("Enter number: "))
s.add(input("Enter number: "))
s.add(input("Enter number: "))

print(s)

input("Press enter to continue...")

