from to_do import TODO


def task6(number):

    result = 0

    while number > 0:
        rem = number % 10
        number = number // 10
        result = (result * 10) + rem

    return result


if __name__ == "__main__":
    print('result is', task6(678))


# https://www.bing.com/videos/search?q=reversed+version+of+the+number.+python&&view=detail&mid=2CC2EBBCB8698653C8F32CC2EBBCB8698653C8F3&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dreversed%2Bversion%2Bof%2Bthe%2Bnumber.%2Bpython%26FORM%3DHDRSC3