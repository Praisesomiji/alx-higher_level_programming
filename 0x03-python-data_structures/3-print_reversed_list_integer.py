#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1

    while (i):
       print("{:d}".format(i))
       i -= 1
print_reversed_list_integer([0, 1, 2, 3])
