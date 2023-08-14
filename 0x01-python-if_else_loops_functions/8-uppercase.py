#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    for i in range(0, strlen):
        n = ord(str[1])
        # if character is in lower case
        if n in range(97, 123):
            n = n - 32
        if i < (strlen - 1):
            print("{:c}".format(n), end='')
        else:
            print("{:c}".format(n), end='\n')
