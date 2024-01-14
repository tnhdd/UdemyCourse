def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


another_operation = False

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    while not another_operation:
        num1 = int(input("What is the first number? "))
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation above ")
        num2 = int(input("What is the second number? "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input("Do you want to do another operation? ")
        if should_continue == "n":
            another_operation = True
        elif should_continue == "y":
            calculator()
