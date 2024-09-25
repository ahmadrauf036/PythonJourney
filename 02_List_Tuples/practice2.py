#sorting in list

numbers=[]
numbers.append(int(input("Enter number: ")))
numbers.append(int(input("Enter number: ")))
numbers.append(int(input("Enter number: ")))
numbers.append(int(input("Enter number: ")))
numbers.append(int(input("Enter number: ")))
numbers.append(int(input("Enter number: ")))

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

input("Press enter to continue...")