class Bank:
    NameofBank="State_Bank"
    @classmethod
    def Change_Name(cls,name):
        cls.NameofBank=name
MyAccount=Bank()
print(f"Before changing of variable i.e. Bank Name :  {MyAccount.NameofBank}")
Bank.Change_Name("Allied_Bank")
print(f"After changing of variable i.e. Bank Name  :  {MyAccount.NameofBank}")