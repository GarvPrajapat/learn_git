class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,obj):
        return Point(self.x + obj.x , self.y + obj.y)
    
    def __sub__(self,obj):
        return Point(self.x - obj.x , self.y - obj.y)

    def __str__(self):
        return f"{{{self.x},{self.y}}}"


print(Point(3,4))