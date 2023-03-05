#!/usr/bin/python3
def no_c(my_string):
    a = len(my_string)
    i = 0
    while i < a:
        if my_string[i] == c or my_string == C:
            my_string.translate({ord(i): None})
        i++
    return my_string

