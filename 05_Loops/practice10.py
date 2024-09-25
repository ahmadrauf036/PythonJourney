#shape 4
'''
****  n=4
*  *
*  *
****

***** n=5
*   *
*   *
*   *
*****

*** n=3
* *
***
'''
n=int(input("Enter number: ")) 

for i in range(n,0,-1):
  if i==n or i==1:
    print("*"*n)
  else:
    print("*"+" "*(n-2)+"*")

