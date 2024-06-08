#!/usr/bin/env python3

from brain_games.cli import welcome_user
import brain_games.game_engine as game_engine


def main():
    name_user = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    game_engine.play_game('gcd', name_user)


if __name__ == '__main__':
    main()
