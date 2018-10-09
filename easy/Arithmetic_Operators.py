def foo(a, b):
    if ((1 <= a and pow(10, 10) >= a) and (1 <= b and pow(10, 10) >= b)):
        print(a + b)
        print(a - b)
        print(a * b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    foo(a, b)
