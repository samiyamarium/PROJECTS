class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Student\'s name:  ",[name],"Student\'s marks: ", [marks])    
    def display(self):
        ""        
st1=Student("Samia",67)
st1.display()
st1=Student("Sami",90)
st1.display()