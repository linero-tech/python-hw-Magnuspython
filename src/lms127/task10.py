from to_do import TODO


def task10_1(assessments):
    return len(assessments)



def task10_2(assessments):
    return assessments[3]



def task10_3(assessments):
    number_of_assessments = len(assessments)
    index_of_middle = int(number_of_assessments / 2)
    middle_assessment = assessments[index_of_middle]
    return middle_assessment
# return assessments[len(assessments) // 2]




def task10_4(assessments):
    result = assessments[0:3]
    return result


if __name__ == "__main__":
    print(task10_4("LMFHM"))
