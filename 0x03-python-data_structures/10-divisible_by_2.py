#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if len(my_list) == 0:
        return new_list
    for i in range(0, len(my_list)):
        new_list.append(my_list[i] % 2 == 0)
    return new_list
