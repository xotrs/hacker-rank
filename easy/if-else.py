#!/bin/python3
def foo(x):
    if x % 2 == 1 and x <= 100:
        return "Weird"
    elif x % 2 == 0 and 5 >= x >= 2:
        return "Not Weird"
    elif x % 2 == 0 and 20 >= x >= 6:
        return "Weird"
    elif x % 2 == 0 and 20 < x <= 100:
        return "Not Weird"


N = foo(int(input()))
print(N)
