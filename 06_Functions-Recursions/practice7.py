def printShape(n:int):
    if(n==0):
        return 0
    
    print("*"*n)
    return printShape(n-1)
    

def main():
    n=int(input("Enter a number: "))
    
    printShape(n)
    
main()
        
        