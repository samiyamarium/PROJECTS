class A:
    def show(self):
        print("Show method in A")

class B(A):
    def show(self):
        print("Show method in B")

class C(A):
    def show(self):
        print("Show method in C")

class D(B, C):
    print("Lets see what D offers\n oh! see below!!")


d = D()
d.show()


print(D.__mro__)
