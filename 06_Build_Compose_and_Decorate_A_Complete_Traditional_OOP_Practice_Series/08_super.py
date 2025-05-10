class Person:
    def __init__(self,name):
        self.name=name
class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject
teacher=Teacher("Sir Ali Jawwad", "Python")
print("Teacher\'s name : ",teacher.name)
print("Teaching subject : ",teacher.subject)