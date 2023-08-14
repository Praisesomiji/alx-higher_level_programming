#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    for i in range(0, strlen):
        n = ord(str[i])
        # if character is in lower case
        if n in range(97, 123):
            n = n - 32
        print("{:c}".format(n), end='')
    print('');
