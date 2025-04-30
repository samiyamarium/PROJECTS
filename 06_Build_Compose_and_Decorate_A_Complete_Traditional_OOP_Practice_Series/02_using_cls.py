class Counter:
    c=0 #initialize counter variable
    def __init__(self):
        Counter.c+=1
    @classmethod
    def display(cls):
        print(f"You have created {cls.c} objects ")
C1=Counter()
C2=Counter()
C3=Counter()
C4=Counter()
C5=Counter()
C6=Counter()
Counter.display()
