print("Hello class")

class Robot:
    """This class will return a object which will cointain name colour of  the robot"""
    """This is a simple class implementation in python. The easiest way to remember class.
Thing to remember is self is nothing but the object name."""
    #Defining Constructors 

    def __init__ (self,name,colour):
        self.name = name
        self.colour=colour

    def hello(self):
        print ("Hello! My name is "+self.name+" and colour is " + self.colour)


#r= Robot("Surya","Red")
#r.hello()