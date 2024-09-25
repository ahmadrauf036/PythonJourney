#student has passed or failed 
#(requires total of 40% & at least 33% in each subject)

english=int(input("Enter English marks: "))
urdu=int(input("Enter Urdu marks: "))
math=int(input("Enter Math marks: "))

if ((english/100)*100)>=33 and ((urdu/100)*100)>=33 and ((math/100)*100)>=33 and (((math+english+urdu)/300)*100)>=40:
    print("Pass")
else:
    print("Fail")
    
input("Press Enter to continue...")