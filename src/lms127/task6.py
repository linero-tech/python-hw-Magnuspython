from to_do import TODO


def task6(base1, base2, height):
    result = (base1 * height + base2 * height) / 2
    return result

if __name__ == "__main__":
    print(task6(base1=10.0, base2=20.0, height=1.0))

    # (b1 * h + b2 * h) / 2