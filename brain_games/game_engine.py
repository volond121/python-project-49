import prompt
from brain_games.games.calc import gat_res_calc
from brain_games.games.even import gat_res_even
from brain_games.games.gcd import gat_res_gcd
from brain_games.games.prime import gat_res_prime
from brain_games.games.progression import gat_res_progression


NUM_ROUNDS = 3  # number of rounds


# checking the player's response
def gat_answer_user(question, result):
    print("Question: " + question)
    answer_use = prompt.string('Your answer: ')
    if answer_use == str(result):
        print('Correct!')
        return True
    else:
        print(f"'{answer_use}' is wrong answer ;(. "
              f"Correct answer was '{result}'.")
        return False


def play_game(game, user_name):
    for i in range(NUM_ROUNDS):
        match game:
            case 'calc':
                (generated_query_string, right_answer) = gat_res_calc()
            case 'even':
                (generated_query_string, right_answer) = gat_res_even()
            case 'gcd':
                (generated_query_string, right_answer) = gat_res_gcd()
            case 'prime':
                (generated_query_string, right_answer) = gat_res_prime()
            case 'progression':
                (generated_query_string, right_answer) = gat_res_progression()
        answer = gat_answer_user(generated_query_string, right_answer)
        if not (answer):
            break
    if not (answer):
        print(f"Let's try again, {user_name}!")
    else:
        print(f"Congratulations, {user_name}!")
