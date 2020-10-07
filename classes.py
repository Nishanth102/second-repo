#create a class
class firstClass:
    '''
    there should be a gap after def
    self is used to call the object itself
    to create a attribute we need to use 
    self.attributeName=attribute value
    '''
    def __init__(self,name,age):
        self.x=name
        self.age=age
    
    def firstClassFunction(self):
        """
        we need to pass self so that the object can call the function
        we can also give an optional parameter-list if required
        return instead of print later on as the function will probably
        be combined and used with print which will then return a None
        and can cause massive confusion
        example print(print('hellow world')) will return 
        hellow world
        None
        """
        print('The age of '+self.x+' is '+str(self.age))
    
#Creating my first object
firstVariable = firstClass('Nishanth',26)
firstVariable.firstClassFunction()

#To check whether the object has the attribut or not
print(hasattr(firstVariable,'x'))  #true
print(hasattr(firstVariable,'age')) #true
print(hasattr(firstVariable,'name')) #false

#To add am attribut to a varibale instead of 
# changing the entire Class
# use setattr -- use for special case object  
setattr(firstVariable,'learning','python')

#To get the value of the attribute we can use getattr
print(getattr(firstVariable,'learning'))

#To delete an attribute from the object use delattr
delattr(firstVariable,'x')
print(hasattr(firstVariable,'x'))

#Creating the child class
class firstChildClass(firstClass):
    """
    Creating my first child class it will inherit all the 
    variables,functions created in the parent class
    """ 
    print('\nChild class is called')        
    def __init__(self):
        print('Child Class has been Initialized')
firstChildVariable = firstChildClass()



#Using Inheritance and super function 
class Parent():
    """
    just a parent calss
    """
    num=10
    age=26
    def __init__(self,var,var1):
        self.x=var
        self.y=var1
    
class Child(Parent):
    """
    just another child class
    """
    def __init__(self,first,second):
        super().__init__(first,second)
        print(super().age)
        print(self.x,self.y)

obj=Child("nishanth","2")

#Another nice example of usign super function for working with
#Multi layered Inheritance



class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)
