import math
from datetime import datetime

# Ask user for an integer with the given prompt.
def getInt(prompt):
    while True:
        i = input(prompt)
        try:
            i = float(i)
        except ValueError:
            continue
        return i

# Attempt to convert given value to an integer.
def tryToInt(i):
    if i % 1 == 0:
        return int(i)
    else:
        return i

# Log the given calculation.
def log(calculation):
    now = datetime.now()
    time = "[" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "]"

    with open("log.txt", "a") as log:
        log.write(time + " " + calculation + "\n")

# Receive and add two numbers.
def addition():
    a = tryToInt(getInt("Enter a number: "))
    b = tryToInt(getInt("Enter another number: "))
    answer = a + b

    calculation = str(a) + "+" + str(b) + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and subtract two numbers.
def subtraction():
    a = tryToInt(getInt("Enter a number: "))
    b = tryToInt(getInt("Enter another number: "))
    answer = a - b
    
    calculation = str(a) + "-" + str(b) + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and multiply two numbers.
def multiplication():
    a = tryToInt(getInt("Enter a number: "))
    b = tryToInt(getInt("Enter another number: "))
    answer = a * b
    
    calculation = str(a) + "*" + str(b) + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and divide two numbers.
def division():
    a = tryToInt(getInt("Enter a number: "))
    b = tryToInt(getInt("Enter another number: "))
    answer = a / b
    
    calculation = str(a) + "/" + str(b) + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and get the exponent of two numbers.
def exponentiation():
    a = tryToInt(getInt("Enter a number: "))
    b = tryToInt(getInt("Enter another number: "))
    answer = a ** b
    
    calculation = str(a) + "^" + str(b) + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and get the square root of a number.
def squareroot():
    a = tryToInt(getInt("Enter a number: "))
    answer = math.sqrt(a)
    
    calculation = "sqrt(" + str(a) + ")" + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Receive and get the factorial of a number.
def factorial():
    while True:
        a = tryToInt(getInt("Enter a number: "))
        if a >= 0 and a % 1 == 0:
            break
    answer = math.factorial(a)
    
    calculation = str(a) + "!" + " = " + str(tryToInt(answer))
    
    print(calculation)
    log(calculation)
    input("")

# Prompt user for an operation to excecute.
def getOperation():
    while True:
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Exponentiation")
        print("6) Square Root")
        print("7) Factorial")

        while True:
            operation = getInt("Operation: ")
            if operation != None and operation % 1 == 0 and operation >= 1 and operation <= 7:
                break

        # Excecute given operation.
        if operation == 1:
            addition()
        elif operation == 2:
            subtraction()
        elif operation == 3:
            multiplication()
        elif operation == 4:
            division()
        elif operation == 5:
            exponentiation()
        elif operation == 6:
            squareroot()
        elif operation == 7:
            factorial()

# Launch calculator.
getOperation()
