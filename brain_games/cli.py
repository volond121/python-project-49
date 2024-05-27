import prompt


def question_and_cheer():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    return name

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