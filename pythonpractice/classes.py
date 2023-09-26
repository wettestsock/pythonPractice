import numpy as npy


#CLASSES ----------


class employee:
    def __init__(self, first, last, pay): #CONSTRUCTOR   , self is plaaceholder for the class
        #parameters for initializing
        
        #when calling self it refers to the instance of that variable within the class
        # makes it not a global variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def full(self): #self declares it as the class instance instead of global instance
        return f'full name:\t{self.first} {self.last}\nincome:\t\t{self.pay}\nemail:\t\t{self.email}\n'
    
    pass # pass means skip (if want to make template)

#self instance is passed automatically
emp1= employee('joe', 'biden', 50000) 
emp2 = employee('hunter', 'biden', 1000000)

print(emp1.full()) # email 

#can run using class name itself
print(employee.full(emp2)) #manually pass instance as the arg, puts self 