class Person:
    def __init__(self,name,age):
        self.name = name  
        self.age = age
        
    def getNameAge(self):
        return f"My name is {self.name} and my age is {self.age}"
    

class Student(Person):
    def __init__(self,name,age,classs):
        super().__init__(name,age)
        self.classs=classs
    def getClass(self):
        return f"{self.name} is in the class {self.classs}"
    
p1 = Person("saif",28)

print(p1.getNameAge())

s1= Student("messi",35,"inter miami")

print(s1.getNameAge())
print(s1.getClass())
 
