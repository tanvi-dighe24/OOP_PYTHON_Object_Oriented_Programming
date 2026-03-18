#static method


*it is a method it is nor and neither related to object and class members.


*to create static method we will make use of decorator called '@staticmethod'.





syntax: class classname:


                -----propertie----


                -----behaviors----


                def __init__(self,propertyname1,propertyname2.......):


                    self.variablename=propertyname1


                    self.variablename=propertyname2


                    .


                    .


                    .



                #modifying object members


                


                def methodname(self,new):


                    ------instructions-----


                @classmethod


                #modify class members


                def methodname(cls,new):


                    ------instructions-----



                @staticmethod


                def methodname(arguments):


                    ----instructions------


                    


                    


                    


         objectname=classname(value1,value2...........valuen)



class School:


    s_name='GGH school'


    s_loc='hyd'



    def __init__(self,name,roll,loc,contact):


        self.name=name


        self.roll=roll


        self.loc=loc


        self.contact=contact



    @classmethod


    def ch_sloc(cls):


        cls.s_loc=cls.get_addr()



    def ch_loc(self):


        self.loc=self.get_addr()



    @staticmethod


    def get_addr():


        return input('enter a new address/loc:')


        



s1=School('prajwal',101,'banglore',7544877556)


s2=School('aarti',102,'banglore',7544877553)


s3=School('renuka',103,'banglore',7544871553)


s4=School('vijaya',104,'banglore',7544677553)


s5=School('jyothi',105,'banglore',7248775538)



print(School.s_name,School.s_loc)


print(s1.name,s1.roll,s1.loc,s1.contact)


#s1.ch_loc()


#print(s1.name,s1.roll,s1.loc,s1.contact)



School.ch_sloc()


print(School.s_name,School.s_loc)





