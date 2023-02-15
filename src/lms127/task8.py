from to_do import TODO


def task8():
    sentence = input('Write an sentence here to count a chooseble character:')
    character = input('Enter a character to count if how many time it occours in the sentence:')
    count = 0
    for x in sentence:
        if x == character:
            count += 1
    print(character, 'occurs', count, 'times')

if __name__ == "__main__":
        task8()