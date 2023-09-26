import numpy as npy


#CLASSES ----------


class employee:
    
    
    #does the same thing as static variable in c++ classes, one instance for all classes    
    raiseAm = 1.04
    # class variable: shared by all classes

    def __init__(self, first, last, pay): #CONSTRUCTOR   , self is plaaceholder for the class
        #parameters for initializing
        
        #when calling self it refers to the instance of that variable within the class
        # makes it not a global variable
        self.first = first   # <--- instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def full(self): #self declares it as the class instance instead of global instance
        return f'full name:\t{self.first} {self.last}\nincome:\t\t{self.pay}\nemail:\t\t{self.email}\n'
    
    def applyRaise(self):
        self.pay = int(self.pay* self.raiseAm)  #raiseAm of the instance rather than 
        

    def makeGlobalRaise(self):
        self.pay = int(self.pay * employee.raiseAm) 


    pass # pass means skip (if want to make template)

#self instance is passed automatically
emp1= employee('joe', 'biden', 50000) 
emp2 = employee('hunter', 'biden', 1000000)

print(emp1.full()) # email 

#can run using class name itself
print(employee.full(emp2)) #manually pass instance as the arg, puts self 



employee.raiseAm=1.10  #changes the raise amount for the entire class

emp1.raiseAm = 1.1    #changes the raise amount for the class instance and makes it a class instance instead
emp1.applyRaise()


employee.raiseAm=1.5

print(emp1.pay) 


print(emp1.__dict__, emp1.pay, employee.raiseAm, sep='\n')
#print(emp1.__dict__)  #shoes all the variables in the instance of the class
print(employee.__dict__, '\n') # shoes all the variables in the class, including classs variables

emp1.makeGlobalRaise()
emp2.makeGlobalRaise()
print(emp1.__dict__, emp1.pay, employee.raiseAm, sep='\n')
print(emp2.__dict__, emp2.pay, employee.raiseAm, sep='\n')