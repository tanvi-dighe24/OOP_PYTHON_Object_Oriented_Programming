#Inheritance:


whatsapp version1--->text-->2 months-->class1


whatsapp version 2--->text,call,status--->2months-->class2



it is a phenomenon of copying the properties of one class to another class



types of inheritance:


1.single level


2.multi level


3.multiple


4.herarchical


5.hybrid inheritance




1.single level:deriving the properties from one parent class to one child class.



syntax:  class parentclassname:


                ----properties---


                ----functionalities---



        class childclassname(parentclassname):


                ----properties---


                ----functionalities---



        


            


'''



class parents:


    house='4bhk'


    land='10 acres'


    vehicle='bike'




class childrens(parents):


    vehicle2='car'




print(childrens.house,childrens.land,childrens.vehicle,childrens. vehicle2)
