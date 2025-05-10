print("Static method to add two numbers")
class MathUtils:
    @staticmethod
    def add(a,b):
        print(f"The sum of {a} and {b} is {a+b}")
        return(a+b)
MathUtils.add(3,8)
    