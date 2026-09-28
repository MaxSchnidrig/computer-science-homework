import re

def alert(text):
    print("-" * len(text))
    print(text.upper())
    print("-" * len(text))
    menu()

def menu():
    math_expression = input("Enter Your Experession: ")
    tokenise(math_expression)

def tokenise(math_expression):
    math_expression = re.split(r"([+\-*/])", math_expression)
    num_of_operators = len(math_expression)/2
    loop_for_operators(math_expression, num_of_operators)


def loop_for_operators(math_expression, num_of_operators):
    n = 1
    result = None
    for x in range (0,int(num_of_operators)):
        operator = math_expression[n]
        if operator == "*":
            result = operator_multiply(math_expression, n, result)
            n = n + 2
        elif operator == "/":
            result = operator_divide(math_expression, n, result)
            n = n + 2
        elif operator == "+":
            result = operator_add(math_expression, n, result)
            n = n + 2
        elif operator == "-":
            result = operator_subtract(math_expression, n, result)
            n = n + 2
    print(result)
    menu()

def operator_add(math_expression, n, result):
    if result is None:
        product = int(math_expression[n - 1]) + int(math_expression[n +1])
    else:
        product = result + int(math_expression[n +1])
    return(product)

def operator_subtract(math_expression, n, result):
    if result is None:
        product = int(math_expression[n - 1]) - int(math_expression[n +1])
    else:
        product = result - int(math_expression[n +1])
    return(product)

def operator_multiply(math_expression, n, result):
    if result is None:
        product = int(math_expression[n - 1]) * int(math_expression[n +1])
    else:
        product = result * int(math_expression[n +1])
    return(product)

def operator_divide(math_expression, n, result):
    if result is None:
        product = int(math_expression[n - 1]) / int(math_expression[n +1])
    else:
        product = result / int(math_expression[n +1])
    return(product)

alert("Welcome to the calculator")

"""
Next steps:

Make it possible to exponentiate
Make it include bedmas with exponentiate no brackets
(Potentially include brackets)

Note, Currently doesn't work:

exponentiating
Bedmas
Negative numbers
Brackets

Note, Currently does work:

Expressions with two same operators
Expressions with two mixed operators
Expressions with any number of mixed operators
"""
