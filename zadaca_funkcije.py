import def_zadaca_funkcije


# Exercise 12.1: The sum of two numbers
def zbroj(x, y):
    print(x + y)


zbroj(5, 6)
zbroj(-2, 3)
zbroj(-1, -9)


# Exercise 12.2: The cube of a number
def cube(x):
    print(x * x * x)


cube(5)
cube(-5)
cube(2.2)

# Exercise 12.3: Steps counter
kalkulator = def_zadaca_funkcije.steps_calculator(20, 5)
print(kalkulator)


# Exercise 12.4: Absolute difference between two numbers:
def abs_diff(x, y):
    print(abs(x) - abs(y))


abs_diff(-5, -2)
abs_diff(5, 2)
abs_diff(-5, 2)
abs_diff(5, -2)
