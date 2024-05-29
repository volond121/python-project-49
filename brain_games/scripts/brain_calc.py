from brain_games.games.b_calc import games_calc
from brain_games.cli import question_and_cheer


def main():
    name_user = question_and_cheer()
    if not (games_calc()):
        print(f"Let's try again, {name_user}!")
    else:
        print(f"Congratulations, {name_user}!")


if __name__ == '__main__':
    main()
