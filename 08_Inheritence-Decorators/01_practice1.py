class twoDVector:
    def __init__(self,i=0,j=0):
        self.i=i
        self.j=j
        
    def __add__(self,newVec:'twoDVector'):
        result=twoDVector()
        result.i=self.i+newVec.i
        result.j=self.j+newVec.j
        return result
    def __sub__(self,newVec:'twoDVector'):
        result=twoDVector()
        result.i=self.i-newVec.i
        result.j=self.j-newVec.j
        return result
    def __str__(self):
        if self.j<0:
            return str(self.i)+'i'+str(self.j)+'j'  
        return str(self.i)+'i+'+str(self.j)+'j'
    def __repr__(self):
        return str(self)

class threeDVector(twoDVector):
    def __init__(self, i=0, j=0,k=0):
        super().__init__(i, j)
        self.k=k
    def __add__(self,newVec:'threeDVector'):
        result=threeDVector()
        result.i=self.i+newVec.i
        result.j=self.j+newVec.j
        result.k=self.k+newVec.k
        return result
    def __sub__(self,newVec:'threeDVector'):
        result=threeDVector()
        result.i=self.i-newVec.i
        result.j=self.j-newVec.j
        result.k=self.k-newVec.k
        return result
    def __str__(self):
        if self.j<0 or self.k<0:
            if self.j<0 and self.k>=0:
                return str(self.i)+'i'+str(self.j)+'j'+'+'+str(self.k)+'k'
            elif self.j>=0 and self.k<0:
                return str(self.i)+'i'+'+'+str(self.j)+'j'+str(self.k)+'k'
            elif self.j<0 and self.k<0:
                return str(self.i)+'i'+str(self.j)+'j'+str(self.k)+'k'
        return str(self.i)+'i'+'+'+str(self.j)+'j'+'+'+str(self.k)+'k'
        
    def __repr__(self):
        return str(self)
    
    
def main():
    vec1=twoDVector(2,-3)
    vec2=twoDVector(4,1)
    result=vec1+vec2
    print("Vector 1: ",vec1)
    print("Vector 2: ",vec2)
    print("Result: ",result)
    
    vecStr=str(vec1)
    print(vecStr,type(vecStr))
    print("----- 3-D Vector -----")
    vec3=threeDVector(1,-2,-3)
    print("Vector 3: ",vec3)
    vec4=threeDVector(4,2,-6)
    print("Vector 4: ",vec4)
    result=vec3+vec4
    print("Result: ",result)
    
main()
    