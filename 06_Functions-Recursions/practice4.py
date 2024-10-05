def factorial(n:int):
    if(n==1):
        return 1
    return n*factorial(n-1)

def main():
    n=int(input("Enter a number: "))
    
    print(factorial(n))
    
main()
        
        