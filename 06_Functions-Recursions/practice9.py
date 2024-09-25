def printShape(n:int,m:int=0):
    if(m==n):
        return 0
    elif(m==0 or m==n-1):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
        
    
    
    return printShape(n,m+1)
    

def main():
    n=int(input("Enter a number: "))
    
    printShape(n)
    
main()
        
        