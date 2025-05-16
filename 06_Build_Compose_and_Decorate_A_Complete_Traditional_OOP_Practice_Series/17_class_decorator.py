def add_greeting(self):
    def greet(self):
        return "Hi!"
    self.greet = greet
    return self

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("sam")
print(p.greet())
