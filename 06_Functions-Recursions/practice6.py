def multiplicationTable(n:int,m:int=10):
    if(m==0):
        return 0
    a=multiplicationTable(n,m-1)+1
    print(f"{n} * {m} = {n*a}")
    return a

def main():
    n=int(input("Enter a number: "))
    
    multiplicationTable(n)
    
main()
        
        