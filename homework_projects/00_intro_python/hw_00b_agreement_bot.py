def main():
    print("Hi! I am a machine and i will tell you about my favourite")

    user=str(input("USER: My favourite colour is ----->>")).lower()
    machine=str(input(f"MACHINE: My favourite colour is also {user}"))

    print(user)
    print(machine)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()