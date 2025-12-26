class student:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def display(self):
        print(f"Name:{self.name} Place:{self.place}")
class school(student):
    def __init__(self, name, place,age,schoolname):
        super().__init__(name, place)
        self.age=age
        self.schoolname=schoolname
    def display1(self):
        super().display()
        print(f"Age:{self.age} Schlname:{self.schoolname}")
a=school("Praveen","Myd",20,"Kalaimahal school")
a.display1()
print(a.name,a.place,a.age,a.schoolname)
   