class Programmer:
    name=""
    age=int()
    lang=""
    codingLang=""
    company="Microsoft"
    
    def __init__(self,name,age,lang,codingLang): #Dunder Method --> Runs automatically
        self.lang=lang
        self.codingLang=codingLang
        self.age=age
        self.name=name
        
    def displayDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nLanguage: {self.lang}\nCoding Language: {self.codingLang}\nCompany: {self.company}")
        return

def main():
    pro1=Programmer("Ahmad Rauf",21,"Urdu","Python")
    pro2=Programmer("Bilal Afzal",26,"English","c#")
    pro3=Programmer("Abdullah Shafiq",20,"Punjabi","Javascript")
    
    pro1.displayDetails()
    pro2.displayDetails()
    pro3.displayDetails()
    
    return

class Programmer:
    name=""
    age=int()
    lang=""
    codingLang=""
    company="Microsoft"
    
    def __init__(self,name,age,lang,codingLang): #Dunder Method --> Runs automatically
        self.lang=lang
        self.codingLang=codingLang
        self.age=age
        self.name=name
        
    def displayDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nLanguage: {self.lang}\nCoding Language: {self.codingLang}\nCompany: {self.company}")
        return

def main():
    pro1=Programmer("Ahmad Rauf",21,"Urdu","Python")
    pro2=Programmer("Bilal Afzal",26,"English","c#")
    pro3=Programmer("Abdullah Shafiq",20,"Punjabi","Javascript")
    
    pro1.displayDetails()
    pro2.displayDetails()
    pro3.displayDetails()
    
    return

main()