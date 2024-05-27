from brain_games.b_even import games_even
from brain_games.cli import question_and_cheer


def main():
    name_user = question_and_cheer()
    if games_even() == "wrong":
        print(f"Let's try again, {name_user}")
        return False
    else:
        print(f"Congratulations, {name_user}")
        return True


if __name__ == '__main__':
    main()
