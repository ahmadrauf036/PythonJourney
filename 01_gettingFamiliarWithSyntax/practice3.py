#string functions 

#f strings
name=input("Enter your name: ")
print(f"Good Afternoon {name}")

from datetime import date
print(f"Dear {name},\nYou are Selected!\n{date.today()}")

#string funtions
sentence="Ahmad is a good boy and he is responsible."
sentence=sentence.replace("good","great").replace("boy","man")
print(sentence)
#Q. if strings are immutable, how can replace function in strings can change it?
#ANS. Replace function create a new string with changes. it doesn't modify the original string.

#Replace double space with single
sentence="ahmad is  good"
index=sentence.find("  ")
print(index)
sentence=sentence.replace("  "," ")
print(sentence)


input("press enter to continue...")