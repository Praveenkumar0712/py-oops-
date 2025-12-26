class animal:
    def __init__(favrt, name, food):
        favrt.name = name
        favrt.food = food 

    def display(favrt):
        print(f"Name:{favrt.name}\nFood:{favrt.food}")
a=animal("cat","fish")  
print(a.name,a.food)  
a.display()
