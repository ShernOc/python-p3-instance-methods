#!/usr/bin/env python3

class Person:
    #Instance method definition/ function 
    def talk(self): # method / function 1. 
        print("Hello World!")
        
    def walk(self): # method/function 2 
        print("The person is walking.")
        
# To call the class we have to have: 
# An instance is created where the object is created "hello" from the Person class. The object (hello) can now use the method talk, defined in class. 
hello = Person()

#Method is called. 
hello.talk()
hello.walk() 