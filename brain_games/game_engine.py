import prompt


NUM_ROUNDS = 3  # number of rounds


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


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


def play_game(game, greeting):
    user_name = welcome_user()
    print(greeting)
    for i in range(NUM_ROUNDS):
        (generated_query_string, right_answer) = game()
        answer = gat_answer_user(generated_query_string, right_answer)
        if not (answer):
            break
    if not (answer):
        print(f"Let's try again, {user_name}!")
    else:
        print(f"Congratulations, {user_name}!")
