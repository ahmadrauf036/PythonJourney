def printShape(n:int):
    if(n==0):
        return 0
    printShape(n-1)
    print("*"*n)
    return 0
    

def main():
    n=int(input("Enter a number: "))
    
    printShape(n)
    
main()
        
        