#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0;
    try:
        while count < x:
            print(my_list[count], end="")
            count += 1
    finally:
        print()
        return count
