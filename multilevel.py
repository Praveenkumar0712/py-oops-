class grandparent:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def display(self):
        print(f"name:{self.name}\n place:{self.place}")
class parent(grandparent):
    def __init__(self,name,place,age,work):
        super().__init__(name,place)
        self.age=age
        self.work=work
    def display1(self):
        print(f"age:{self.age}\n work:{self.work}\n") 
class child (parent):
    def __init__(self,name,place,age,work,salary,duration):
        super(). __init__(name,place,age,work)
        self.salary=salary
        self.duration=duration
    def display2(self):
        super().display()
        print(f"name:{self.name}\n place:{self.place}age:{self.age}\n work:{self.work}\nsalaly:{self.salary}\n duration:{self.duration}")
a=child("Rajkumar","Chennai",34,"ITmanager","25k","6month")
a.display2()
print(a.name,a.place,a.age,a.work,a.salary,a.duration)           


     
