from to_do import TODO


def task2(number):
    result = is_prime = True
    if number > 1:


        for divisor in range(2, number):
            if (number % divisor) == 0:
                result = False
                break
            else:
                is_prime = True

    return result

if __name__ == "__main__":
    print(task2(5))