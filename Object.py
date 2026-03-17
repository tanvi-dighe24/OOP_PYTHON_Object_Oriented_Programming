'''
#OBject: instance of class
Real world entity created from blueprint(Class).

Objects: Hold data (attributes) & can plan perform actions(Methods).

#Creation Of Object:
obj_name= class_name(arg)

#Accessing object members:
obj_name.obj_name_member

-we can create Unlimited objects from class.
-object data store in Heap Memory.

#After Deleting object:
Python garbage collector frees memory automatically.
#Garbage Collector:
When creates objects in python, they use memory (RAM).

-If object is no longer needed (no variable is reffering to it).
-it becomes Garbage.
-Python has Build in process called Garbage Collector(GC) that automatically frees memory used by such unused objects.
'''

class Bank:
     bank_name= 'SBI'  #class variable
     bank_location= 'Mysore' #class variable

c1= Bank() 
c2= Bank()
