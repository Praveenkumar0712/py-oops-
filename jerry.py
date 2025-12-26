class student:
    def __init__(self, name, age,place):
        self.name = name
        self.age = age
        self.place=place

    def display(self):
        print(f"Name: {self.name},\t Age: {self.age},\t Place: {self.place}")
a=student("jerry", 20,"chennai")
print(a.name,a.age,a.place)
a.display()    
