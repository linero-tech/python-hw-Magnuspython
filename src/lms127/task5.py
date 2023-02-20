


def task5(value_for_a, value_for_b):
    a = value_for_a
    b = value_for_b
    a, b = b, a

    return a,b


if __name__ == "__main__":
    print (task5(1, 2))
