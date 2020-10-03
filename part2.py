from part1 import Robot
class part2:
    def __init__ (self,speed,name):
        self.speed=speed
        self.name=name

    def RoboSpeed(self):
        print("Name from other class:"+self.name)
        print("My speed is "+ self.speed)

cl1=Robot("Surya","Reds")
cl2 =part2('60kmh',cl1.name)

cl1.hello()
cl2.RoboSpeed()
        


