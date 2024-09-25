#shape 3
'''
    *       1
   ***      3
  *****     5
 *******    7
*********   9

  *
 ***
*****
'''
n=int(input("Enter number: ")) 
c=1
for i in range(n,0,-1):
  print(" "*(i-1)+"*"*c)
  c+=2

