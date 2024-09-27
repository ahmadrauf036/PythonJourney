import math

class Calculator:
    validOp={'+','-','/','*','sqrt','^'}
    def __init__(self):
        self.num1=int()
        self.num2=int()
        self.op=""
        
    @staticmethod
    def menu():
        print("Welcome to my Calculator!")
        print("\nInstructions:")
        print("This is a simple calculator that can perform following operatins:")
        print("Addition, Subtraction, Multiplication, Division, exponent and Square root")
        print("\nHow to use it:")
        print("1. Enter the operands and operators at specified places.\n2. Enter operators carefully;")
        print("+, *, -, /, ^power, sqrt (for square root)")
        return
    
    def takeInput(self):
        self.num1=int(input("Enter 1st operand: "))
        self.op=input("Enter operator: ")
        if self.op not in self.validOp and not self.op.startswith('^'):
            print("Invalid operator")
            return 0
        if self.op[0]=='^' or self.op=='sqrt':
            return 1
        
        self.num2=int(input("Enter 2nd operand: "))
        return 1
    
    def addition(self):
        return self.num1+self.num2
    
    def multiplication(self):
        return self.num1*self.num2
    
    def division(self):
        if self.num2==0:
            print("Division by 0 is undefined!")
            return -1
        return self.num1/self.num2
    
    def subtraction(self):
        return self.num1-self.num2
    
    def exponent(self):
        p=int(self.op.split('^')[1])
        return self.num1**p
    
    def squareRoot(self):
        if self.num1>=0:
            return math.sqrt(self.num1)
        else:
            return "Square root of negative numbers is not real!"
        
    def calculations(self):
        if(self.op=='+'):
            return self.addition()
        elif(self.op=='*'):
            return self.multiplication()
        elif(self.op=='/'):
            return self.division()
        elif(self.op=='-'):
            return self.subtraction()
        elif(self.op[0]=='^'):
            return self.exponent()
        elif(self.op=='sqrt'):
            return self.squareRoot()

        print("Error!")
        return -1
    
    def openCalculator(self):
        self.menu()
        if self.takeInput():
            self.result()
        return
    
    def result(self):
        result=self.calculations()
        if result!=-1:
            print("result:",result)
        else:
            print("Error!")
        return
    
    
def main():
    cal1=Calculator()
    cal1.openCalculator()
    
    cal2=Calculator()
    cal2.openCalculator()
    print("--------------------------------")
    
    cal1.result()
    cal2.result()
    
    return

main()