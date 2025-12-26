class parent:
    def __init__ (self,name,age):
     self.name=name 
     self.age=age
    def display (self):
     print(f"name:{self.name},age:{self.age}")
a=parent("praveen","23")
print(a.name,a.age)
a.display()  
