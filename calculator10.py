# ===============================
# MEGA SCIENTIFIC CALCULATOR
# ===============================

import math

# -------- BASIC OPERATIONS --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# -------- ADVANCED OPERATIONS --------
def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)

def modulus(a, b):
    return a % b

def absolute(a):
    return abs(a)

def factorial(a):
    if a < 0:
        return "Error: Negative number"
    return math.factorial(int(a))

# -------- TRIGONOMETRY --------
def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

# -------- LOGARITHMS --------
def log_base_10(a):
    if a <= 0:
        return "Error: Invalid input"
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        return "Error: Invalid input"
    return math.log(a)

# -------- MENU --------
def show_menu():
    print("\n========= MEGA CALCULATOR =========")
    print("1  -> Add")
    print("2  -> Subtract")
    print("3  -> Multiply")
    print("4  -> Divide")
    print("5  -> Power")
    print("6  -> Square Root")
    print("7  -> Modulus")
    print("8  -> Absolute Value")
    print("9  -> Factorial")
    print("10 -> Sin")
    print("11 -> Cos")
    print("12 -> Tan")
    print("13 -> Log base 10")
    print("14 -> Natural Log")
    print("15 -> Show Memory")
    print("0  -> Exit")
    print("==================================")

# -------- MAIN PROGRAM --------
memory = 0

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Calculator closed. Goodbye 👋")
        break

    if choice == "15":
        print("Memory value:", memory)
        continue

    try:
        if choice in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                memory = add(a, b)
            elif choice == "2":
                memory = subtract(a, b)
            elif choice == "3":
                memory = multiply(a, b)
            elif choice == "4":
                memory = divide(a, b)
            elif choice == "5":
                memory = power(a, b)
            elif choice == "7":
                memory = modulus(a, b)

        elif choice in ["6", "8", "9", "10", "11", "12", "13", "14"]:
            a = float(input("Enter number: "))

            if choice == "6":
                memory = square_root(a)
            elif choice == "8":
                memory = absolute(a)
            elif choice == "9":
                memory = factorial(a)
            elif choice == "10":
                memory = sine(a)
            elif choice == "11":
                memory = cosine(a)
            elif choice == "12":
                memory = tangent(a)
            elif choice == "13":
                memory = log_base_10(a)
            elif choice == "14":
                memory = natural_log(a)
        else:
            print("Invalid choice")
            continue

        print("Result:", memory)

    except ValueError:
        print("Error: Please enter valid numeric input")
