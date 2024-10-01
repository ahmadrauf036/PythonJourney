class Employee:
    def __init__(self,name="Unknown",salary:float=0):
        self.name=name
        self.salary=salary
    
    @property
    def increment(self):
        return self.salary
    @increment.setter
    def increment(self,inc:float):
        self.salary+=inc
    
def main():
    e=Employee()
    e.increment=80
    print(e.salary)
main()