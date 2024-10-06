from functools import reduce

l=[1,2,3,4,5,6,7]

print(list(map(lambda x:x*x,l)))
print(list(filter(lambda x:x%2==0,l)))
print(reduce(lambda a,b:a+b,l))