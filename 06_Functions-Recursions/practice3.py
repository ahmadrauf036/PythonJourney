def sumOfNaturalNumbers(n:int):
    if(n==1):
        return 1
    return n+sumOfNaturalNumbers(n-1)

def main():
    n=int(input("Enter a number: "))
    
    print(sumOfNaturalNumbers(n))
    
main()
        
        