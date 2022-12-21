class Robot:
    def __init__(self,name,weight,color):
        self.name = name
        self.weight = weight
        self.color = color
    def introduce(self):
        print("My name is " + self.name)
r1 = Robot('MAX',50,'Magenta')
r1.introduce()