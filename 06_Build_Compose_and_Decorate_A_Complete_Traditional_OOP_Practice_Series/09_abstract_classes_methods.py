from abc import ABC,abstractmethod
class Shape(ABC):

   @abstractmethod
   def area(self):
    ""
class Rectangle(Shape):

  def __init__(self,width,height):
    self.width=width
    self.height=height
  def area(self):
    return self.width*self.height
rect=Rectangle(9,5)
print("The area of rectangle is : " , rect.area())
