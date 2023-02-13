from to_do import TODO


def task6():
    b1 = float(input('input base 1:'))
    b2 = float(input('input base 2:'))
    h = float(input('input height:'))
    area = (b1 * h + b2 * h) / 2
    print('result is = ', area)

if __name__ == "__main__":
    task6()