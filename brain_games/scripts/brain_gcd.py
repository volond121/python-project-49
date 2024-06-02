#!/usr/bin/env python3

from brain_games.games.b_gcd import games_gcd
from brain_games.cli import question_and_cheer
import brain_games.games_fun as games_fun


def main():
    name_user = question_and_cheer()
    print("Find the greatest common divisor of given numbers.")
    games_fun.result_us(games_gcd(games_fun.NUM_ROUNDS), name_user)


if __name__ == '__main__':
    main()
