def main():
    print("This program adds and subtracts two numbers.")
    num1 : str = input("Enter first number: ")
    num1  = float(num1)
    num2  : str = input("Enter second number: ")
    num2  = float(num2)
    total = f"{num1} and {num2} adds to make : {num1 + num2} & \n{num1} and {num2} Subtracts to make: {num1-num2}"
    print("Results : \n" + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()