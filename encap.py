class pk:
    def __init__ (self,name,age):
        self.__name=name
        self.__age=age
    def gettername(self):
        return self.__name
    def getterage(self):
        return self.__age
    def settername(self,name,age):
        self.__name=name
        self.__age=age
       
dp=pk("pk",3)
print(dp.gettername())
dp.settername("praveen",23)
print (dp.gettername())
print(dp.getterage())
