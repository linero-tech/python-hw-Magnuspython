from to_do import TODO


def task3(number):
    if number == 1:
        return 1
    else:
        return number * task3(number - 1)



if __name__ == "__main__":
    print("result is", task3(5))


