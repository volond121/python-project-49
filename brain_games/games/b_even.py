import random
from brain_games.games_fun import answer_user


def colc_resoult_even(nambe_for_qustion):
    remain = nambe_for_qustion % 2
    if (remain == 0):
        answer_true = "yes"
    else:
        answer_true = "no"
    return answer_true

def games_even(rounds):
    for i in range(rounds):
        nambe_for_qustion = random.randint(1, 100)
        answer = answer_user(str(nambe_for_qustion), colc_resoult_even(nambe_for_qustion), 'int_arg')
        if not (answer):
            return False

    return True
