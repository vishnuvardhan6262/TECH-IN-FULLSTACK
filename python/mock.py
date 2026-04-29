l=[5,10,15,20,25,30]
from functools import reduce
# sq=list(map(lambda x:x**2,l))
# fi=list(filter(lambda x:x%5==0,sq))
# print(reduce(lambda x,y:x+y,fi))

k=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,l)))
print(k)

class Employee:
    min_exp=2
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def display(self):
        if self.experience >=Employee.min_exp:
            print("Eligible for Promotion")
    @staticmethod
    def update(cls):
        Employee.min_exp+=2
    @staticmethod
    def valid(department):
        if department=="HR" or "Tech" or"Admin":
            print("Valid")

obj=Employee("sai",3,"IT")
obj.display()
obj.update(10)
obj.valid("HR")


#16





class Hero:
    def __init__(self,name,health,is_alive):
        self.name=name
        self.is_alive=is_alive
        self.health=health
    def take_damage(self,amount):
        self.health-=amount
        if self.health<=0:
            self.health==0
            self.is_alive=False
        print(self.health)
    def heal(self,amount):
        if self.health<=0:
            print("Cannot heal a fallen Hero")
        else:
            self.health+=self.amount
obj=Hero("sasi",100,True)
obj.take_damage(10)
obj.heal(20)












