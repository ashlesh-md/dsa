import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="first number")
    parser.add_argument("--operation", help="operation")
    args = parser.parse_args()

    number1 = int(args.number1)
    number2 = int(args.number2)
    operation = args.operation

    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "mul":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2 if number2 != 0 else "Can't Devide By Zero")
    else:
        print("Invalid Operation")
