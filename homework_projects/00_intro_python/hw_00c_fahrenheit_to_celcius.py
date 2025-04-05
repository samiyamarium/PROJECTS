def main():
    print("Convert fahrenheit to celcius")

    degrees_fahrenheit=float(input("Enter temperature in fahranheit to convert : "))
    degrees_celcius=(degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperature : {degrees_fahrenheit} equivalent to {degrees_celcius} degree celcius")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()