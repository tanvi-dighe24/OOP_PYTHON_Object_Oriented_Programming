#what is oop: object oriented programming, it provide structure to coding by using class and objects., class is like datatype
#class: it is blueprint for maling class, class is like a container inwhich methods n properties present.
#Object: get created via class, thats why known as instance of class. they are like variable. in object methods n attributes are working.
#Diff. between Class & Object: class has blueprint to create objects, class define on time but we can make many objects or we can simply create 0 objects also by pass statement under class.
#Class Creation : by using class keyword we start creating class forwarded by class_name which follows pascal and identifier rules. End with colon (:)
#Object Crwation: obj_name(arg)
#Constructor: automatic creates when object creates, same name as class_name, 1)default 2)cooy 3)parametric
#__init__() method: after object creates get called thats y called in constructor. for object work implementation
#self in python: used in oop, object has self as argument

#-------

#inheritance: its oop important property, where child class carries inheritance from their parent class.

#Hybrid Inheritance: Food Order apps : Zomato, Swiggy
class food_app:
    def start(self):
        print('start food ordering app')
class zomato(food_app):
    def order(self):
        print('no item found')
class swiggy(food_app):
    def order(self):
        print('order is not under budget')
class tanvi(food_app):
    def order(self):
        print('order if in budget of 1000')

#adv. of inheritance: allow child classes to copy  parent class properties
#types of inheritance: there are total 5 types, single-level,multi-level,hybrid,multiple,hierachical

#----------
#polymorphism: its a imp concept from oop, in which poly-many and morphism: change. that means object behaves in different ways.
#method overloading: same kind of funtion has many version. also has different parameters.
#method overriding: there must be 2 classes - parent and child in which child class defines method of parent class with same name it overrides parent metod

#operator_overloading proggram:

class school_pay:
    def __init__(self, student):
        self.student = student
    def __add__(self, other):    
        return self.student + other.student

object1 = school_pay(123000)
object2 = school_pay(32000)
print(object1 + object2)         


                 
