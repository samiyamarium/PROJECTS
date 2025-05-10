class Employee:
    def __init__(self,name,salary,serviceid):
        self.name=name #public
        self._salary=salary #protected
        self.__serviceid=serviceid #private
e1=Employee("Samiya",200000,"45A9l2")
print("Public Variable",e1.name)
print("Protected Variable",e1._salary)
print("Private Variable",e1.__serviceid)
