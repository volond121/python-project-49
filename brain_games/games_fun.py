import prompt


NUM_ROUNDS = 3  # number of rounds


# checking the player's response
def answer_user(str_qust, result, viwe_arg):
    print("Question: " + str_qust)
    answer_use = prompt.string('Your answer: ')
    if viwe_arg == 'int_arg':
        if answer_use == str(result):
            print('Correct!')
            return True
        else:
            print(f"'{answer_use}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            return False


def result_us(result_answer, user_name):
    if not (result_answer):
        print(f"Let's try again, {user_name}!")
    else:
        print(f"Congratulations, {user_name}!")
