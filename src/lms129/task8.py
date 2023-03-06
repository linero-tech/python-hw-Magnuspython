from to_do import TODO


def task8(number):

    result = 0
    for digit in str(number):
        result += int(digit)
    return result

if __name__ == "__main__":
    print("result is", task8(123))


# https://www.geeksforgeeks.org/python-program-for-sum-the-digits-of-a-given-number/