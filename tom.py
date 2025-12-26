class student:
    def __init__(details, name, age,place):
        details.name = name
        details.age = age
        details.place=place

    def display(details):
        print(f"Name: {details.name}\t Age: {details.age}\tPlace: {details.place}")
a=student("jerry", 20 ,"chennai")
b=student("tom  ", 22,"bangalore")
c=student("micky", 21,"hyderabad")
d=student("rosey", 19,"pune")
e=student("")
print(a.name,a.age,a.place)
print(b.name,b.age,b.place)
print(c.name,c.age,c.place)
print(d.name,d.age,d.place)
print(e.name,e.age,e.place)
a.display()    
b.display()
c.display() 
d.display()