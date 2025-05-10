class Logger:
    def __init__(self):
        print("Logger is created")
    def __del__(self):
        print("The Logger is destroyed")
log=Logger()
del log