class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, v):
        return f" Multiply: {v * self.factor} , Ex-OR : {v^self.factor},  Addition : {v + self.factor} "


d= Multiplier(2)


print(callable(d))
result = d(23)
print(f"Three operations multiplication, Ex-OR, Addition are performed respectively :  {result}")
