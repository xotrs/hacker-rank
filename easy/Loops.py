def foo(number):
    if 0 <= number <= 20:
        for i in range(0, number):
            print(pow(i, 2))


if __name__ == '__main__':
    n = int(input())
    foo(n)
