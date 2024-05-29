import random
from brain_games.cli import answer_user


def games_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        nambe_for_qustion = random.randint(1, 100)
        remain = nambe_for_qustion % 2
        if (remain == 0):
            answer_true = "yes"
        else:
            answer_true = "no"
        answer = answer_user(str(nambe_for_qustion), answer_true, 'int_arg')
        if not (answer):
            return False

    return True
