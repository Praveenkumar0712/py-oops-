class vechiel:
    def color(self):
       return "searching for color"
    def size(self):
       return "searching for size"
    def speed(self):
       return "finding speed"
class car(vechiel):
   def color(self):
      return ""
   def size(self):
      return "small"
   def speed(self):
      return "high"
class bike(vechiel):
   def color(self):
    return "white"
   def size(self):
      return "medium"
   def speed(self):
      return "slow"
vechies=[car(),bike()]
for types in vechies:
   print(types.color())
   print(types.size())
   print(types.speed())

   