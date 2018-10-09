def is_leap(year):
    leap = False

    if 1900 <= year <= pow(10, 5):
        # leap year case
        # 400으로 나누어떨어지면 무조건 leap year
        # 4로 나누어떨어지는데 100으로 나누어 떨어지면 윤년이 아님
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap = True

    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
