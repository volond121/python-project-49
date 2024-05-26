from brain_games.b_even import games_even


def main(name_user):
    if games_even() == "wrong":
        print(f"Let's try again, {name_user}")
        return False
    else:
        print(f"Congratulations, {name_user}")
        return True


if __name__ == '__main__':
    name_user = "User"
    main(name_user)
