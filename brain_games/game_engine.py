import prompt


NUM_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def run_round(question, expected_result):
    print("Question: " + question)
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(expected_result):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{expected_result}'.")
        return False


def play_game(get_round_params, greeting):
    user_name = welcome_user()
    print(greeting)
    for i in range(NUM_ROUNDS):
        (generated_query_string, right_answer) = get_round_params()
        answer = run_round(generated_query_string, right_answer)
        if not (answer):
            break
    if not (answer):
        print(f"Let's try again, {user_name}!")
    else:
        print(f"Congratulations, {user_name}!")
