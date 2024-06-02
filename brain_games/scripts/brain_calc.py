#!/usr/bin/env python3

from brain_games.games.b_calc import games_calc
from brain_games.cli import question_and_cheer
import brain_games.games_fun as games_fun


def main():
    name_user = question_and_cheer()
    print("What is the result of the expression?")
    games_fun.result_us(games_calc(games_fun.NUM_ROUNDS), name_user)


if __name__ == '__main__':
    main()
