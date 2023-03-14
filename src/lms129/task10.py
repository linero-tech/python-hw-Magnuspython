from to_do import TODO


def task10(password):
    has_lowercase = False
    has_special_character = False
    has_uppercase = False
    has_number = False
    has_correct_length = len(password) in range(6, 11)

    return has_lowercase and has_special_character and has_uppercase and has_number and has_correct_length

if __name__ == "__main__":
    print(task10(password= "abc"))