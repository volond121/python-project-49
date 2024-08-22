#!/usr/bin/env python3

from brain_games.games.calc import get_round_params_calc
import brain_games.game_engine as game_engine


def main():
    game_engine.play_game(get_round_params_calc,
                          "What is the result of the expression?")


if __name__ == '__main__':
    main()
