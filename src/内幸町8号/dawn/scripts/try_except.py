try:
    for i in [-2, -1, 0, 1, 2]:
        print(1 / i)
except ZeroDivisionError as e:
    print(e)