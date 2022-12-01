#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(args):
    if not len(args) == 4:
        print(f"Usage: {arg[0]} a operator b")
        exit(1)

    op = args[2]
    a = args[1]
    b = args[3]

    if op == '+':
        print(f"{a} + {b} = {add(a, b)}")
        exit(0)
    elif op == '-':
        print(f"{a} - {b} = {sub(a, b)}")
        exit(0)
    elif op == '*':
        print(f"{a} - {b} = {mul(a, b)}")
        exit(0)
    elif op == '/':
        print(f"{a} - {b} = {div(a, b)}")
        exit(0)
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)


def exit(status):
    sys.exit(status)


if __name__ == '__main__':
    calculate(sys.args)
