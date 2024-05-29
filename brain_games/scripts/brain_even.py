from brain_games.games.b_even import games_even
from brain_games.cli import question_and_cheer


def main():
    name_user = question_and_cheer()
    if not (games_even()):
        print(f"Let's try again, {name_user}!")
    else:
        print(f"Congratulations, {name_user}!")


if __name__ == '__main__':
    main()
